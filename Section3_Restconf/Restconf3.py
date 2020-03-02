#!/usr/bin/env python

import json
import requests
from requests.auth import HTTPBasicAuth


#
auth = HTTPBasicAuth('cisco', 'cisco')
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json'
}

# when you add ?deep to the url, you get back all child elements for the RESTCONF API on IOS-XE.
# without ?deep in the url you won't get back all child elements for the RESTCONF API on IOS-XE.

url = 'https://192.168.0.200/restconf/data/Cisco-IOS-XE-native:native/interface?fields=Vlan/ip/address/primary;Vlan/name'
response = requests.get(url, headers=headers, auth=auth, verify=False)

response = json.loads(response.text)
print(json.dumps(response, indent=2))

