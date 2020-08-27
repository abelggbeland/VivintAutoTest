import requests
from requests.auth import HTTPBasicAuth
import json


#desktop 19330
#SD 19318
#BeCfzeHG6qOayU4uz3585F6D


url = "https://vivint.atlassian.net/rest/api/3/issue/SD-72841/"

auth = HTTPBasicAuth("abel.beland@vivint.com", "BeCfzeHG6qOayU4uz3585F6D")

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))