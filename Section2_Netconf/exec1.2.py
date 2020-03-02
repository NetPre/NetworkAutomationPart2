from Newbinding import openconfig_interfaces
from pyangbind.lib.serialise import pybindIETFXMLEncoder
import json
#https://github.com/robshakir/pyangbind


op_if = openconfig_interfaces()


NewInt = op_if.interfaces.interface.add('Ten1/0/1')


print(json.dumps(NewInt.get(),indent=2))


NewInt.config.description='something cool'



print(json.dumps(NewInt.get(),indent=2))

print('<config>'+pybindIETFXMLEncoder.serialise(NewInt)+'</config>')

