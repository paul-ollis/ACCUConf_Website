def get_proposal_type(info):
    typeMap = {
        "quick": QuickProposalType,
        "interactive": InteractiveProposalType,
        "miniworkshop": MiniWorkshopProposalType,
        "workshop": WorkshopProposalType,
        "fulldayworkshop": FullDayWorkshopType,
        "keynote": KeynoteProposalType,
    }
    result = typeMap.get(info, ProposalType)();
    if isinstance(result, ProposalType): # we have to handle the case that in the database are partly the wrong encoded values stored
        if info == "15 minutes":
            result = QuickProposalType()
        elif info[:20] == "90 minutes, Interact":
            result = InteractiveProposalType()
        elif info[:20] == "90 minutes, Mini Wor":
            result = MiniWorkshopProposalType()
        elif info[:20] == "180 minutes, Worksho":
            result = WorkshopProposalType()
        elif info[:20] == "6 hour workshop":
            result = FullDayWorkshopType()
        elif info[:20] == "60 minutes, Keynote":
            result = KeynoteProposalType()

    return result


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
        return self.__proposal_type.get("id", "NoTypeSet")


class InteractiveProposalType(ProposalType):
    interactive = {
        "id": "interactive",
        "name": "90 minutes, Interactive",
        "hidden": False
    }

    def __init__(self):
        super().__init__(self.interactive)


class MiniWorkshopProposalType(ProposalType):
    mini_workshop = {
        "id": "miniworkshop",
        "name": "90 minutes, Mini Workshop",
        "hidden": False
    }

    def __init__(self):
        super().__init__(self.mini_workshop)


class WorkshopProposalType(ProposalType):
    workshop = {
        "id": "workshop",
        "name": "180 minutes, Workshop",
        "hidden": False
    }

    def __init__(self):
        super().__init__(self.workshop)


class QuickProposalType(ProposalType):
    quick = {
        "id": "quick",
        "name": "15 minutes",
        "hidden": False
    }

    def __init__(self):
        super().__init__(self.quick)


class FullDayWorkshopType(ProposalType):
    keynote = {
        "id": "fulldayworkshop",
        "name": "6 hour workshop",
        "hidden": False
    }

    def __init__(self):
        super().__init__(self.keynote)


class KeynoteProposalType(ProposalType):
    keynote = {
        "id": "keynote",
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
