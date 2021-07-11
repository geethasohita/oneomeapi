from app import ma
from app.models import Vaccine


class VaccineSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vaccine