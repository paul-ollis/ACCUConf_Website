#!/usr/bin/env python3

"""
This is the script to set the value of the role so as to enable registered users to become reviewers.
"""

import sys

from pathlib import Path
from typing import List

from sqlalchemy import create_engine, MetaData, Table, or_


def set_user_as_reviewer(db_path: Path, emails_path: Path) -> None:
    """
    Find all the records for people in the email list who are marked as 'user' and mark them as 'reviewer'.
    """
    engine = create_engine('sqlite:///' + str(db_path.absolute()))
    tables = engine.table_names()
    table_name = 'user_infos'
    if table_name not in tables:
        print('Database file, {}, does not contain a {} table.'.format(db_path, table_name))
        sys.exit(2)
    table = Table(table_name, MetaData(), autoload=True, autoload_with=engine)
    emails = open(str(emails_path.absolute())).read().split()
    engine.execute(table.update().where(or_(table.c.user_id == email for email in emails)).where(table.c.role == 'user').values(role='reviewer'))


def main(args: List[str]) -> None:
    if len(args) != 2:
        name = Path(__file__).name
        print('Usage: {} <db-to-update> <file-of-reviewer-emails>'.format(name))
        sys.exit(1)
    db_path = Path(args[0])
    db_exists = db_path.is_file()
    emails_path = Path(args[1])
    emails_exists = emails_path.is_file()
    if not db_exists:
        print('Database file, {}, does not exist.'.format(db_path))
    if not emails_exists:
        print('Emails file, {}, does not exist.'.format(emails_path))
    if not (db_exists and emails_exists):
        sys.exit(1)
    set_user_as_reviewer(db_path, emails_path)


if __name__ == '__main__':
    main(sys.argv[1:])
