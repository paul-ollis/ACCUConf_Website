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
    def __init__(self, proposaltype={}):
        self.__proposal_type = proposaltype

    def proposalType(self):
        return self.__proposal_type.get("name", "NoTypeSet")


class InteractiveProposalType(ProposalType):
    interactive = {
        "name": "90 minutes, Interactive",
        "hidden": False
    }

    def __init__(self):
        super().__init__(self.interactive)


class MiniWorkshopProposalType(ProposalType):
    mini_workshop = {
        "name": "90 minutes, Mini Workshop",
        "hidden": False
    }

    def __init__(self):
        super().__init__(self.mini_workshop)


class WorkshopProposalType(ProposalType):
    workshop = {
        "name": "180 minutes, Workshop",
        "hidden": False
    }

    def __init__(self):
        super().__init__(self.workshop)


class QuickProposalType(ProposalType):
    quick = {
        "name": "15 minutes",
        "hidden": False
    }

    def __init__(self):
        super().__init__(self.quick)


class KeynoteProposalType(ProposalType):
    keynote = {
        "name": "60 minutes, Keynote",
        "hidden": True
    }

    def __init__(self):
        super().__init__(self.keynote)


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
