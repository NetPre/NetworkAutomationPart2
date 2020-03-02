from lxml import etree as ET
from ncclient import manager
import xml.dom.minidom
import xmltodict
from binding import openconfig_interfaces
import json


Host = '192.168.0.200'
Port = 830
User = 'cisco'
Pass = 'cisco'

m =  manager.connect(host = Host,port = Port,
                    username=User,password=Pass,
                    hostkey_verify=False,) 


CS_LD = 'http://cisco.com/ns/yang/Cisco-IOS-XE-lldp-oper'
ns_map = {'CS_LD': CS_LD}
env = ET.Element(ET.QName('filter'), nsmap=ns_map)
head = ET.SubElement(env, ET.QName(CS_LD, 'lldp-entries'), nsmap=ns_map)
xmlFilter = ET.tostring(env, pretty_print=True).decode('ascii')
#print(xmlFilter)
xmlLldpNeighbor = m.get(xmlFilter)
#print(xmlLldpNeighbor)


dicLldpInt = xmltodict.parse(xmlLldpNeighbor.data_xml)
#print(dicLldpInt)

for i in dicLldpInt['data']['lldp-entries']['lldp-entry']:
    print(i)


def fixName(oldname):
    return oldname.replace('Te','TenGigabitEthernet')


op_if = 'http://openconfig.net/yang/interfaces'
ns_map = {'op_if': op_if}
env = ET.Element(ET.QName('filter'), nsmap=ns_map)
head = ET.SubElement(env, ET.QName(op_if, 'interfaces'), nsmap=ns_map)

for i in dicLldpInt['data']['lldp-entries']['lldp-entry']:
    #print(i)
    interface = ET.SubElement(head, ET.QName('interface'), nsmap=ns_map)
    name = ET.SubElement(interface, ET.QName('name'), nsmap=ns_map)
    name.text = fixName(i['local-interface'])

xmlFilter = ET.tostring(env, pretty_print=True).decode('ascii')
#print(xmlFilter)

xmlInterfaces = m.get_config(source='running',filter = xmlFilter).data_xml
#print(xmlInterfaces)


dictInterfaces = xmltodict.parse(xmlInterfaces)

#print(json.dumps(dictInterfaces,indent=2))

configChanges = {}
configChanges['config']=dictInterfaces['data']
#print(json.dumps(configChanges,indent=2))



for inti in configChanges['config']['interfaces']['interface']:
#    print(inti['config']['description'])   
#    print(inti["name"]["#text"]) 
    for lldpi in dicLldpInt['data']['lldp-entries']['lldp-entry']:
#        print(lldpi)
        if inti["name"]["#text"]==fixName(lldpi['local-interface']):
            #print(inti['config']['description'],'          ',lldpi['local-interface'])
            inti['config']['description'] = 'neighbor interface'+lldpi['connecting-interface']

#print(json.dumps(configChanges,indent=2))

xmlConfigChange = xmltodict.unparse(configChanges)
print(xmlConfigChange)

output = m.edit_config(target='running',config=xmlConfigChange)
print(output)

m.close_session()

