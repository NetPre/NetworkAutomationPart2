from ietf_ip_binding import ietf_interfaces
import json

model = ietf_interfaces()
model.get()

new_interface = model.interfaces.interface.add('TenGigabitEthernet1/0/3')
#print(json.dumps(new_interface.get(),indent = 2))
new_interface.description = 'NETCONF-CONFIGURED PORT'
print(json.dumps(new_interface.get(),indent = 2))

import pyangbind.lib.pybindJSON as pybindJSON

json_data = pybindJSON.dumps(model, mode='ietf')
with open('new_interface.json','w')as f:
    f.write(json_data)
print (json_data)

