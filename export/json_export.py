def create_json(data):
    return {
        "first_name": data.get("first_name"),
        "email": data.get("email"),
        "plz": data.get("plz")
    }
