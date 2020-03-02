from lxml import etree as ET
from ncclient import manager
import xml.dom.minidom
import xmltodict
from binding import openconfig_interfaces

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

        
m.close_session()

