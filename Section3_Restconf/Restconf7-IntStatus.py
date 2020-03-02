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


url = 'https://192.168.0.200/restconf/data/ietf-interfaces:interfaces-state/interface=GigabitEthernet1%2F0%2F2'


response = requests.get(url, headers=headers, auth=auth, verify=False)


print(response)

print(response.text)


