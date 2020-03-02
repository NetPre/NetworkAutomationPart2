


import json
import requests
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth('arista','arista')
url = "https://192.168.122.196/command-api"

payload = {
  "jsonrpc": "2.0",
  "method": "runCmds",
  "params": {
    "format": "json",
    "timestamps": False,
    "autoComplete": False,
    "expandAliases": False,
    "cmds": [
      "enable ",
      "configure",
      "interface loopback 0",
      "ip address 1.1.1.1/32"
    ],
    "version": 1
  },
  "id": "anything"
}

headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data = json.dumps(payload),auth=auth,verify = False)

response = json.loads(response.text)

print(response)

