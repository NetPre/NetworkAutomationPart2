
from ncclient import manager
import xml.dom.minidom
import xmltodict

Host = '192.168.0.200'
Port = 830
User = 'cisco'
Pass = 'cisco'

with manager.connect(host = Host,
                                    port = Port,
                                    username=User,
                                    password=Pass,
                                    hostkey_verify=False,
                                    timeout= 200, 
                                    allow_agent=False,
                                    look_for_keys=False,
                                    ) as m:


    MyFilter ='''
    <filter>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
		<interface>
			<name>TenGigabitEthernet1/0/1</name>
		</interface>
		<interface>
			<name>TenGigabitEthernet1/0/2</name>
		</interface>
		<interface>
			<name>TenGigabitEthernet1/0/3</name>
		</interface>
    </interfaces-state>
    </filter>
    '''


    runningConfig = m.get(filter=MyFilter).data_xml
    dom =  xml.dom.minidom.parseString(runningConfig) #or xml.dom.minidom.parse(c)
    pretty_xml_as_string = dom.toprettyxml()
    #print(pretty_xml_as_string)

    interfaceDic = xmltodict.parse(runningConfig)
    #print(interfaceDic)

    import json

    #print(json.dumps(interfaceDic,indent=2))

    interfaceStat = interfaceDic['data']["interfaces-state"]["interface"]
#    print(interfaceStat)

    print(json.dumps(interfaceStat,indent=2))

    for i in interfaceStat:
      print(i["name"]['#text'])
