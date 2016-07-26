#!/usr/bin/env python


class ProposalCategory(object):
    C = {
        "name": "C",
        "description": "The C Programming Language"
    }
    CPP = {
        "name": "C++",
        "description": "The C++ Programming Language"
    }
    JVM = {
        "name": "JVM and Languages",
        "description": "The Languages that run on JVM"
    }


class ProposalType(object):
    interactive = {
        "name": "90 minutes, Interactive",
        "hidden": False
    }
    mini_workshop = {
        "name": "90 minutes, Mini Workshop",
        "hidden": False
    }
    workshop = {
        "name": "180 minutes, Workshop",
        "hidden": False
    }
    quick = {
        "name": "15 minutes",
        "hidden": False
    }
    keynote = {
        "name": "60 minutes, Keynote",
        "hidden": True
    }



class ProposalState(object):
    def __init__(self, state = None):
        self.__state = state

    def state(self):
        return self.__state


class NewProposal(ProposalState):
    def __init__(self):
        super().__init__("NEW")


class InReviewProposal(ProposalState):
    def __init__(self):
        super().__init__("IN_REVIEW")


class AcceptedProposal(ProposalState):
    def __init__(self):
        super().__init__("ACCEPTED")


class RejectedProposal(ProposalState):
    def __init__(self):
        super().__init__("REJECTED")


class WaitlistedProposal(ProposalState):
    def __init__(self):
        super().__init__("WAITLISTED")
