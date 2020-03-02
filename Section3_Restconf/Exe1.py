import requests
import json

url = "https://192.168.0.200:443/restconf/data/openconfig-interfaces:interfaces/interface?fields=name;state/oper-status"

payload = {}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28='
}

response = requests.request("GET", url, headers=headers, data = payload,verify = False)
interfacesOut = response.json()
#print(json.dumps(interfacesOut,indent=2))
interfaceListChangeConfig = []
for i in interfacesOut['openconfig-interfaces:interface']:
  if i['state']['oper-status']!='NOT_PRESENT':
    interfaceListChangeConfig.append(i['name'])

interfaceListChangeConfig.pop(interfaceListChangeConfig.index('TenGigabitEthernet1/0/5'))
interfaceListChangeConfig.pop(interfaceListChangeConfig.index('Vlan1'))
interfaceListChangeConfig.pop(interfaceListChangeConfig.index('GigabitEthernet0/0'))
print(interfaceListChangeConfig)






url = "https://192.168.0.200:443/restconf/data/openconfig-interfaces:interfaces/interface"


payload = {"openconfig-interfaces:interface": []}


for i in interfaceListChangeConfig:
  payload["openconfig-interfaces:interface"].append(
    {
    "name": i,
    "config": {
      "description": "ConfiguredWithRestConfonPython"
    },
    "openconfig-if-ethernet:ethernet": {
      "openconfig-vlan:switched-vlan": {
        "config": {
          "interface-mode": "ACCESS",
          "access-vlan": 100
        }
      }
    }
  }
  )

headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28='
}

payload = json.dumps(payload,indent=2)

#print(payload)
response = requests.request("PATCH", url, headers=headers, data = payload,verify=False)

print(response.text.encode('utf8'))

