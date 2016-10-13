from accuconf import db


class MathPuzzle(db.Model):
    __tablename__ = 'mathpuzzles'
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Integer, nullable=False)

    def __init__(self, answer):
        self.answer = answer
