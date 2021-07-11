from flask import request, jsonify

from app import app, db
from app.models import Vaccine
from app.schemas import VaccineSchema

vaccine_schema = VaccineSchema()


@app.route('/')
def index():
    return 'Hello Oneome'


@app.route('/vaccine', methods=['POST'])
def create_vaccine():
    name = request.json.get('vaccine_name')
    company = request.json.get('produced_company')
    min_age = request.json.get('min_age')
    max_age = request.json.get('max_age')
    fda_approved = request.json.get('fda_approved')
    vaccine = Vaccine(vaccine_name=name, produced_company=company, min_age=min_age, max_age=max_age,
                      fda_approved=fda_approved)
    db.session.add(vaccine)
    db.session.commit()
    return vaccine_schema.jsonify(vaccine), 201
