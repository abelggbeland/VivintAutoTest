import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://aggb.atlassian.net/rest/api/3/issue"
auth = HTTPBasicAuth("abelbeland@gmail.com", "TzF6ZbumZRfIPEzae53c9E4B")

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def send(data):
    payload = json.dumps({
    "fields": {
      "issuetype": {
       "name": "Service Request"
      },
      "project": {
        "key": "ABEL"
      },
      "summary": "User " + str(data.getBadgeID()) + " returned",
      "description": {
        "type": "doc",
        "version": 1,
        "content": [
          {
            "type": "paragraph",
            "content": [
              {
                "text": "The user " + str(data.getBadgeID()) + " returned " + str(data.getAssets()) + " They also returned " + str(data.getPeripherals()),
                "type": "text"
              }
            ]
          }
        ]
      },
      "assignee": {
        "accountId": "5f1620059e8ba30016f67baa"
      }
    }
    })


    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))