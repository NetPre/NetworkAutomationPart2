from ncclient import manager
import xml.dom.minidom
import xmltodict
import xml.etree.ElementTree as ET


Host = '192.168.0.200'
Port = 830
User = 'cisco'
Pass = 'cisco'

def getyang(yangName,netconf_connection):
    schema = netconf_connection.get_schema(yangName)
    root = ET.fromstring(schema.xml)
    yang_text = list(root)[0].text
    with open(yangName+'.yang','w') as f :
        f.write(yang_text)



netconf_connection = manager.connect(host = Host,
                                    port = Port,
                                    username=User,
                                    password=Pass,
                                    hostkey_verify=False,
                                    #timeout= 200, 
                                    allow_agent=False,
                                    look_for_keys=False,
                                    )


#print(netconf_connection)
#http://cisco.com/yang/cisco-ia?module=cisco-ia&revision=2018-08-03


  

yangList = ['ietf-yang-types','ietf-interfaces','openconfig-yang-types','openconfig-types','openconfig-inet-types','openconfig-interfaces',
'openconfig-vlan','openconfig-yang-types','openconfig-extensions','openconfig-if-aggregate','openconfig-if-ethernet','openconfig-if-ip'
,'iana-if-type','Cisco-IOS-XE-lldp']

yangList = ['openconfig-local-routing','openconfig-policy-types']
for i in yangList:
    getyang(i,netconf_connection)


netconf_connection.close_session()

