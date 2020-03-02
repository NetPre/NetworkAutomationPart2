#!/usr/bin/env python

import json
import requests
from requests.auth import HTTPBasicAuth


#
auth = HTTPBasicAuth('user', 'password')
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json'
}


body = {
  "ietf-interfaces:interface": {
    "name": "GigabitEthernet2/0/2",
    "description": "o;1 A",
    "type": "iana-if-type:ethernetCsmacd",
    "enabled": 'true',
    "ietf-diffserv-target:diffserv-target-entry": [
      {
        "direction": "ietf-diffserv-target:inbound",
        "policy-name": "Input-Policy-1P3Q1T"
      },
      {
        "direction": "ietf-diffserv-target:outbound",
        "policy-name": "1P3Q1T"
      }
    ],
    "ietf-ip:ipv4": {
    },
    "ietf-ip:ipv6": {
    }
  }
}

url = 'https://10.99.2.104/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2%2F0%2F2'






response = requests.put(url, headers=headers, data=json.dumps(body),auth=auth, verify=False)


print(response)

print(response.text)





