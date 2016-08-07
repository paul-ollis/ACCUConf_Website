#!/usr/bin/env python
import re
from accuconf.models import *


def validateEmail(email):
    emailPattern = re.compile("^([a-zA-Z0-9_.+-])+@(([a-zA-Z0-9-_])+\.)+([a-zA-Z0-9])+$")
    if emailPattern.search(email):
        u = User.query.filter_by(user_id=email).first()
        if u:
            return False
        else:
            return True
    else:
        return False


def validatePassword(passwd):
    if (re.search("\\d", passwd) and re.search("[a-z]", passwd) and
        re.search("[A-Z]", passwd) and len(passwd) >= 8):
        return True
    else:
        return False


def validateProposalData(proposalData):
    mandatoryKeys = ["title", "abstract", "proposalType", "presenters"]
    for key in mandatoryKeys:
        if key not in proposalData:
            return False, "%s information is not present in proposal" % (key)

    if type(proposalData["presenters"]) != list:
        return False, "presenters data is malformed"

    if len(proposalData.get("title")) < 5:
        return False, "Title is too short"

    if len(proposalData.get("abstract")) < 50:
        return False, "Proposal too short"

    return True, "validated"
