import re


def person_data_validation(data: dict) -> list:
    errors = []
    is_matched = re.match(r'^\+[0-9]{7,14}$', data["phone_number"])
    if not is_matched:
        errors.append(
            "Phone number must be in international format: +3801234567891"
        )

    is_matched = re.match(
        r'^([a-zA-Z])+([a-zA-Z ]+[a-zA-Z]+)?$', data["first_name"]
    )
    if not is_matched:
        errors.append(
            "First name must contain only letters"
        )

    is_matched = re.match(
        r'^([a-zA-Z])+([a-zA-Z ]+[a-zA-Z]+)?$', data["last_name"]
    )
    if not is_matched:
        errors.append(
            "Last name must contain only letters"
        )

    return errors
