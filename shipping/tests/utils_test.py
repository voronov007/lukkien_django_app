from ..utils.forms import person_data_validation


def test_person_data_validation_errors():
    data = {
        "phone_number": "12345678",
        "first_name": "John88",
        "last_name": "J+"
    }
    errors = person_data_validation(data)
    assert len(errors) == 3
    assert errors[0] == "Phone number must be in international format: +3801234567891"
    assert errors[1] == "First name must contain only letters"
    assert errors[2] == "Last name must contain only letters"


def test_person_data_validation_ok():
    data = {
        "phone_number": "+3912345678",
        "first_name": "Un Ci",
        "last_name": "Lin"
    }
    errors = person_data_validation(data)
    assert len(errors) == 0
