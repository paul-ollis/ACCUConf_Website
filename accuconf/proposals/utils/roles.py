#!/usr/bin/env python


class Role(object):

    admin = {
        "name": "admin",
        "description": "Super Admin"
    }
    reviewer = {
        "name": "reviewer",
        "description": "Reviews, votes and comments on proposals"
    }
    user = {
        "name": "user",
        "description": "Can submit proposals and reply to comments on them"
    }
