
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
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
		<interface>
			<name>FortyGigabitEthernet1/1/1</name>
		</interface>
    </interfaces>
    </filter>
    '''


    runningConfig = m.get_config(source='running',filter=MyFilter).data_xml
    dom =  xml.dom.minidom.parseString(runningConfig) #or xml.dom.minidom.parse(c)
    pretty_xml_as_string = dom.toprettyxml()
    print(pretty_xml_as_string)

    MyFilter ='''
    <filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
		<interface>
			<name>FortyGigabitEthernet1/1/1</name>
		</interface>
    </interfaces>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
		<interface>
			<name>FortyGigabitEthernet1/1/1</name>
		</interface>
    </interfaces-state>
    </filter>
    '''


    runningConfig = m.get(filter=MyFilter).data_xml
    dom =  xml.dom.minidom.parseString(runningConfig) #or xml.dom.minidom.parse(c)
    pretty_xml_as_string = dom.toprettyxml()
    print(pretty_xml_as_string)
