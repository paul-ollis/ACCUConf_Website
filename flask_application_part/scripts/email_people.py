#!/usr/bin/env python3

"""
This script is for emailing some people who have submitted proposals.

This script handles command line handling and the actual emailing. The subject
line and the email body template are given as command line arguments, as is
the name of the database to query. The fourth argument is the path to a
Python module with an SQLAlchemy query function. This module is loaded and
the query run on the database to provide the list of contacts to send to. The
items in the list should be tuples (email, first-name, last-name).
"""

import importlib
import sys

from email.mime.text import MIMEText
from email.utils import formatdate
from smtplib import SMTP

from pathlib import Path
from typing import List, Tuple

from sqlalchemy import create_engine

# The order here is critical for the way main works.
_emailout_filenames = ('subject.txt', 'text.txt', 'query.py')


def _exiting(exit_code: int) -> None:
    """
    Print an exiting message and then exit with the exit code provided.
    """
    print('Exiting with code {}.'.format(exit_code))
    sys.exit(exit_code)


def query_database(database_file_path: Path, query_module_path: Path) -> List:
    """
    Load the query module, execute the query on the database and
    return the result.
    """
    module_name = query_module_path.stem
    module_location = query_module_path.absolute().parent
    if module_location:
        sys.path.append(str(module_location))
    try:
        module = importlib.import_module(module_name)
        engine = create_engine('sqlite:///' + str(database_file_path.absolute()))
        return list(engine.execute(module.query(engine)))
    except ImportError as e:
        print('Error:', e.msg)
        _exiting(2)


def send_email(subject: str, text: str, recipients: List[Tuple[str, str, str]]):
    """
    Open a connection to an SMTP server and send emails to all the
    contacts discovered by the query.
    """
    print('Subject:', subject)
    print('Recipients:', recipients)
    with SMTP('smtp.winder.org.uk') as server:
        for person in recipients:
            email, fname, lname = person
            message = MIMEText(text, _charset='utf-8')
            message['From'] = 'conference@accu.org'
            message['To'] = '{} {} <{}>'.format(fname, lname, email)
            message['Cc'] = 'russel@winder.org.uk'
            message['Subject'] = subject
            message['Date'] = formatdate()  # RFC 2822 format.
            server.send_message(message)


def main(args: List[str]) -> None:
    arg_labels = ('emailout-name', 'database-file-path')
    if len(args) != 2:
        print('Usage: email_people.py <{}> <{}>'.format(*arg_labels))
        sys.exit(1)
    args_labels = tuple(zip(args, arg_labels))
    ok_to_proceed = True
    for arg, label in args_labels:
        if len(arg) == 0:
            print('Empty {}.'.format(label.replace('-', ' ')))
            ok_to_proceed = False
    if not ok_to_proceed:
        _exiting(1)
    ok_to_proceed = True
    emailout_files = tuple(Path(Path(__file__).parent.parent / 'emailouts' / args[0] / item) for item in _emailout_filenames)
    for arg in emailout_files:
        if not arg.is_file():
            print('Cannot find file: {}'.format(arg))
            ok_to_proceed = False
    if not ok_to_proceed:
        _exiting(1)
    # Same order as names in _emailout_filenames
    subject_file_path, text_file_path, query_file_path = emailout_files
    with open(str(subject_file_path)) as subject_file, open(str(text_file_path)) as text_file:
        subject = subject_file.read().strip()
        text = text_file.read().strip()
        send_email(subject, text, query_database(Path(args[1]), query_file_path))


if __name__ == '__main__':
    main(sys.argv[1:])