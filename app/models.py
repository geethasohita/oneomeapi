from app import db


class Vaccine(db.Model):
    vaccine_id = db.Column(db.Integer, primary_key=True)
    vaccine_name = db.Column(db.String(64), unique=True, nullable=False)
    produced_company = db.Column(db.String(64), nullable=False)
    min_age = db.Column(db.Integer, nullable=False)
    max_age = db.Column(db.Integer, nullable=False)
    fda_approved = db.Column(db.Boolean, nullable=False)