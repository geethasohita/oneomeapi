from app import app, db
from app.models import Vaccine


@app.route('/')
def index():
    return 'Hello Oneome'


@app.route('/vaccine', methods=['POST'])
def create_vaccine():
    vaccine = Vaccine(vaccine_name='test', produced_company='test', min_age=20, max_age=100, fda_approved=False)
    db.session.add(vaccine)
    db.session.commit()
    return 'Success'