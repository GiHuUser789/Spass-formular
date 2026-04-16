import re

def is_valid_email(email):
    return re.fullmatch(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None

def is_valid_plz(plz):
    return re.fullmatch(r"\d{5}", plz) is not None
