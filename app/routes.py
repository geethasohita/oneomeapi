from flask import request
from app import app, db
from app.schemas import VaccineSchema
from app.service import OneOmeService

vaccine_schema = VaccineSchema()
vaccines_schema = VaccineSchema(many=True)
service = OneOmeService(db)


@app.route('/')
def index():
    return 'Hello Oneome'


@app.route('/vaccine', methods=['POST'])
def create():
    name = request.json.get('vaccine_name')
    company = request.json.get('produced_company')
    min_age = request.json.get('min_age')
    max_age = request.json.get('max_age')
    fda_approved = request.json.get('fda_approved')
    vaccine = service.create_vaccine(name=name, company=company, min_age=min_age, max_age=max_age, fda_approved=fda_approved)
    return vaccine_schema.jsonify(vaccine), 201


@app.route('/vaccine', methods=['GET'])
def get():
    name = request.args.get('name')
    vaccines = service.get_vaccines(name)
    return vaccines_schema.jsonify(vaccines), 200


@app.route('/vaccine/<vaccine_id>', methods=['PUT'])
def modify(vaccine_id):
    name = request.json.get('vaccine_name')
    company = request.json.get('produced_company')
    min_age = request.json.get('min_age')
    max_age = request.json.get('max_age')
    fda_approved = request.json.get('fda_approved')
    vaccine = service.modify_vaccine(vaccine_id, name, company, min_age, max_age, fda_approved)
    return vaccine_schema.jsonify(vaccine), 202


@app.route('/vaccine/<vaccine_id>', methods=['DELETE'])
def delete(vaccine_id):
    vaccine = service.delete_vaccine(vaccine_id)
    return vaccine_schema.jsonify(vaccine), 202
