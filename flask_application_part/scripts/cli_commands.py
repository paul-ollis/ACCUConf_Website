
# This must be imported here even though it may not be explicitly used in this file.
import click

import sys

from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

file_directory = Path(__file__).absolute().parent
sys.path.insert(0, str(file_directory.parent))

from accuconf import app, db
from accuconf.models import User, UserInfo, UserLocation, Proposal, ProposalPresenter, ProposalReview, ProposalComment


@app.cli.command()
def create_database():
    """Create an initial database."""
    db.create_all()


@app.cli.command()
def all_reviewers():
    """Print a list of all the registrants labelled as a reviewer."""
    for x in UserInfo.query.filter_by(role='reviewer').all():
        print('{} {} <{}>'.format(x.first_name, x.last_name, x.user_id))


@app.cli.command()
def committee_are_reviewers():
    """Ensure consistency between committee list and reviewer list."""
    file_name = 'committee_emails.txt'
    try:
        with open(str(file_directory / file_name)) as committee_email_file:
            committee_emails = {s.strip() for s in committee_email_file.read().split()}
            reviewer_emails = {u.user_id for u in UserInfo.query.filter_by(role='reviewer').all()}
            committee_not_reviewer = {c for c in committee_emails if c not in reviewer_emails}
            reviewers_not_committee = {r for r in reviewer_emails if r not in committee_emails}
            print('Committee members not reviewers:', committee_not_reviewer)
            print('Reviewers not committee members:', reviewers_not_committee)
    except FileNotFoundError:
        print('{} not present in directory {}.'.format(file_name, file_directory))


@app.cli.command()
def create_proposal_sheets():
    """Create the bits of papers for constructing an initial schedule."""
    file_path = str(file_directory.parent / 'proposal_sheets.pdf')
    style_sheet = getSampleStyleSheet()['BodyText']
    style_sheet.fontSize = 18
    style_sheet.leading = 22
    document = SimpleDocTemplate(file_path, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
    elements = []
    for p in Proposal.query.all():
        table = Table([
            [Paragraph(p.title, style_sheet), p.session_type],
            [', '.join('{} {}'.format(pp.first_name, pp.last_name) for pp in p.presenters),
             ', '.join(str(r.score) for r in p.reviews)],
        ], colWidths=(400, 150), spaceAfter=36)
        table.setStyle(TableStyle([
            ('FONTSIZE', (0, 0), (-1, -1), 12),
        ]))
        elements.append(table)
    document.build(elements)
