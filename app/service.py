from app import db
from app.exceptions import BadRequestException
from app.models import Vaccine


def create_vaccine(name, company, min_age, max_age, fda_approved):
    existing_vaccine = get_vaccines(name)
    if existing_vaccine.count() > 0:
        raise BadRequestException(f'Vaccine with name {name} already exists in database.')
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
    if not vaccine:
        raise BadRequestException(f'Vaccine with id {vaccine_id} does not exist in database.')
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
    if not vaccine:
        raise BadRequestException(f'Vaccine with id {vaccine_id} does not exist in database.')
    db.session.delete(vaccine)
    db.session.commit()
    return vaccine
