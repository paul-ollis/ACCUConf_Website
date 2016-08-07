#!/usr/bin/env python

from accuconf import db


class MathPuzzle(db.Model):
    __tablename__ = 'mathpuzzles'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(10), nullable=False)
    answer = db.Column(db.String(8), nullable=False)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
