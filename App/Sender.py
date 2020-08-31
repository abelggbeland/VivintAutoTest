import requests
from requests.auth import HTTPBasicAuth
import json
import base64

def send(payload, url):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    f = open("Credentials")
    auth = HTTPBasicAuth(base64.b64decode((f.readline().strip()).encode()).decode(), base64.b64decode(f.readline().encode()).decode())
    f.close()

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

    return response.json()


def get(url):
    headers = {
        "Accept": "application/json"
    }

    f = open("Credentials")
    auth = HTTPBasicAuth(base64.b64decode((f.readline().strip()).encode()).decode(),
                         base64.b64decode(f.readline().encode()).decode())
    f.close()

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

    return response.json()
