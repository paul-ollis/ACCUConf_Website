#!/usr/bin/env python

from email.message import Message
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

class MailTemplates(object):
    registration_pending = """
        Hello %s %s,
            Welcome to ACCUConf, the conference for developers,
            professionals. You or someone claiming to be you have registered
            as a user for this conference. If you have done so, please follow this URL.

            %s

            Otherwise, our sincere apologies for the inconvenience. Please
            ignore this email.

            Thank you,
            ACCUConf team.

    """

    registered = """
        Hello %s %s,
            Welcome to ACCUConf, your registration for the ACCU Conference is successful.
            Please visit the conference page at %s to submit a proposal or to learn more
            about the conference.

            Thank you,
            ACCUConf team
    """


class Mailer(object):
    pass
