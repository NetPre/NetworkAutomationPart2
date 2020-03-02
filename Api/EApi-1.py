


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
      "show version",
      "show interfaces"
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


print(json.dumps(response,indent=2))

print('#########################'*10)
interfaceOne = response['result'][1]["interfaces"]['Ethernet1']
print(json.dumps(interfaceOne,indent=2))

