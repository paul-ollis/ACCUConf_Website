#!/usr/bin/env python
import re


def validateEmail(email):
    emailPattern = re.compile("^([a-zA-Z0-9_.+-])+@(([a-zA-Z0-9-_])+\.)+([a-zA-Z0-9])+$")
    if emailPattern.search(email):
        from accuconf.models import User
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

        if proposalData[key] is None:
            return False, "%s information should not be empty" % (key)
    if type(proposalData["presenters"]) != list:
        return False, "presenters data is malformed"

    if len(proposalData["presenters"]) < 1:
        return False, "At least one presenter needed"

    if len(proposalData.get("title")) < 5:
        return False, "Title is too short"

    if len(proposalData.get("abstract")) < 50:
        return False, "Proposal too short"

    (result, message) = validatePresenters(proposalData["presenters"])
    if not result:
        return result, message

    return True, "validated"


def validatePresenters(presenters):
    mandatoryKeys = ["lead", "email", "fname", "lname", "country", "state"]
    leadFound = False
    leadPresenter = ""
    for presenter in presenters:
        for key in mandatoryKeys:
            if key not in presenter:
                return False, "%s attribute is mandatory for Presenters" % (key)

            if presenter[key] is None:
                return False, "%s attribute should have valid data" % (key)

        if "lead" in presenter and "email" in presenter:
            if presenter["lead"] and leadFound:
                return False, "%s and %s are both marked as lead presenters" \
                       % (presenter["email"], leadPresenter)
            elif presenter["lead"] and not leadFound:
                leadFound = True
                leadPresenter = presenter["email"]

    return True, "validated"
