from app import db
from app.models import Vaccine


def create_vaccine(name, company, min_age, max_age, fda_approved):
    vaccine = Vaccine(vaccine_name=name, produced_company=company, min_age=min_age, max_age=max_age,
                      fda_approved=fda_approved)
    db.session.add(vaccine)
    db.session.commit()
    return vaccine


def get_vaccines(name):
    if name:
        vaccines = Vaccine.query.filter(Vaccine.vaccine_name == name)
    else:
        vaccines = Vaccine.query.all()
    return vaccines


def modify_vaccine(vaccine_id, name, company, min_age, max_age, fda_approved):
    vaccine = Vaccine.query.get(vaccine_id)
    vaccine.vaccine_name = name
    vaccine.produced_company = company
    vaccine.min_age = min_age
    vaccine.max_age = max_age
    vaccine.fda_approved = fda_approved
    db.session.add(vaccine)
    db.session.commit()
    return vaccine


def delete_vaccine(vaccine_id):
    vaccine = Vaccine.query.get(vaccine_id)
    db.session.delete(vaccine)
    db.session.commit()
    return vaccine
