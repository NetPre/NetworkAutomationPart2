
from ncclient import manager
import xml.dom.minidom
import xmltodict
from binding import openconfig_interfaces
from Newbinding import openconfig_interfaces
from pyangbind.lib.serialise import pybindIETFXMLEncoder
import json
#https://github.com/robshakir/pyangbind

Host = '192.168.0.200'
Port = 830
User = 'cisco'
Pass = 'cisco'


def fixName(oldname):
    return oldname.replace('Te','TenGigabitEthernet')

with manager.connect(host = Host,
                                    port = Port,
                                    username=User,
                                    password=Pass,
                                    hostkey_verify=False,
                                    ) as m:


    MyFilter ='''
    <filter>
    <lldp-entries xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-lldp-oper"/>
    </filter>
    '''


    runningConfig = m.get(filter=MyFilter).data_xml
    dom =  xml.dom.minidom.parseString(runningConfig) #or xml.dom.minidom.parse(c)
    pretty_xml_as_string = dom.toprettyxml()
    #print(pretty_xml_as_string)

    dicLldpInt = xmltodict.parse(pretty_xml_as_string)
    #print(dicLldpInt['data']['lldp-entries']['lldp-entry'])

    for i in dicLldpInt['data']['lldp-entries']['lldp-entry']:
        #print(i)
        op_if = openconfig_interfaces()
        NewInt = op_if.interfaces.interface.add(fixName(i['local-interface']))
        NewInt.config.description='connected to '+i['device-id']+' on Int '+ i['connecting-interface']
        config = '<config>'+pybindIETFXMLEncoder.serialise(op_if.interfaces)+'</config>'
        #print(config)
        output = m.edit_config(target='running',config=config)
        print(output)

        