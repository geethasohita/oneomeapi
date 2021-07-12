import unittest
from unittest import mock
from unittest.mock import MagicMock

from app.exceptions import BadRequestException
from app.models import Vaccine
from app.service import OneOmeService


class TestMethods(unittest.TestCase):

    def test_create_vaccine(self):
        mock_db = MagicMock()
        service = OneOmeService(mock_db)
        mock_get_vaccines = MagicMock()
        mock_get_vaccines.return_value = []
        service.get_vaccines = mock_get_vaccines

        actual_value = service.create_vaccine(name='test', company='test', min_age=12, max_age=100, fda_approved=True)

        assert actual_value.vaccine_name == 'test'
        assert actual_value.produced_company == 'test'
        assert actual_value.min_age == 12
        assert actual_value.max_age == 100
        assert actual_value.fda_approved

    def test_create_vaccine_exception(self):
        mock_db = MagicMock()
        service = OneOmeService(mock_db)
        mock_get_vaccines = MagicMock()
        mock_get_vaccines.return_value = [Vaccine(vaccine_name='test', produced_company='test', min_age=10, max_age=20,
                                                  fda_approved=True)]

        service.get_vaccines = mock_get_vaccines

        with self.assertRaises(BadRequestException):
            service.create_vaccine(name='test', company='test', min_age=10, max_age=20, fda_approved=True)

    @mock.patch('app.service.Vaccine')
    def test_get_vaccine_by_name(self, mock_vaccine):
        mock_db = MagicMock()
        service = OneOmeService(mock_db)

        vaccine = Vaccine(vaccine_name='test', produced_company='test', min_age=10, max_age=20,
                          fda_approved=True)
        mock_vaccine.query.filter(Vaccine.vaccine_name == 'test').all.return_value = [vaccine]
        actual_value = service.get_vaccines('test')

        assert len(actual_value) == 1
        assert actual_value == [vaccine]

    @mock.patch('app.service.Vaccine')
    def test_get_all_vaccines(self, mock_vaccine):
        mock_db = MagicMock()
        service = OneOmeService(mock_db)

        vaccine = Vaccine(vaccine_name='test', produced_company='test', min_age=10, max_age=20,
                          fda_approved=True)
        mock_vaccine.query.all.return_value = [vaccine]
        actual_value = service.get_vaccines(None)

        assert len(actual_value) == 1
        assert actual_value == [vaccine]

    @mock.patch('app.service.Vaccine')
    def test_modify_vaccine(self, mock_vaccine):
        mock_db = MagicMock()
        service = OneOmeService(mock_db)
        vaccine = Vaccine(vaccine_name='test', produced_company='test', min_age=10, max_age=20, fda_approved=True)
        mock_vaccine.query.get.return_value = vaccine

        actual_value = service.modify_vaccine(vaccine_id=1, name='new_test', company='new_test', min_age=12,
                                              max_age=100,
                                              fda_approved=False)

        assert actual_value.vaccine_name == 'new_test'
        assert actual_value.produced_company == 'new_test'
        assert actual_value.min_age == 12
        assert actual_value.max_age == 100
        assert not actual_value.fda_approved

    @mock.patch('app.service.Vaccine')
    def test_modify_vaccine_exception(self, mock_vaccine):
        mock_db = MagicMock()
        service = OneOmeService(mock_db)
        mock_vaccine.query.get.return_value = None

        with self.assertRaises(BadRequestException):
            service.modify_vaccine(vaccine_id=1, name='new_test', company='new_test', min_age=12,
                                   max_age=100, fda_approved=False)

    @mock.patch('app.service.Vaccine')
    def test_delete_vaccine(self, mock_vaccine):
        mock_db = MagicMock()
        service = OneOmeService(mock_db)
        vaccine = Vaccine(vaccine_name='test', produced_company='test', min_age=10, max_age=20, fda_approved=True)
        mock_vaccine.query.get.return_value = vaccine

        actual_value = service.delete_vaccine(vaccine_id=1)

        assert actual_value.vaccine_name == 'test'

    @mock.patch('app.service.Vaccine')
    def test_delete_vaccine_exception(self, mock_vaccine):
        mock_db = MagicMock()
        service = OneOmeService(mock_db)
        mock_vaccine.query.get.return_value = None

        with self.assertRaises(BadRequestException):
            service.delete_vaccine(vaccine_id=1)


if __name__ == '__main__':
    unittest.main()
