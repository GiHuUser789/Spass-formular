import requests
from export.json_export import create_json

def send_data_to_api(data):
    url = "https://httpbin.org/post"

    payload = create_json(data)

    response = requests.post(url, json=payload)

    return response
