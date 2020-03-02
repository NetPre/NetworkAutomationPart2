
from ncclient import manager
import xml.dom.minidom
import xmltodict
from ncclient import manager, xml_
from jinja2 import Template
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



        configChangesTemp = '''
        <config>
        <interfaces xmlns="http://openconfig.net/yang/interfaces">
        {% for i in intList%}
                        <interface>
                                <name xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">{{i}}</name>
                                <ethernet xmlns="http://openconfig.net/yang/interfaces/ethernet">
                                        <switched-vlan xmlns="http://openconfig.net/yang/vlan">
                                                <config>
                                                        <interface-mode>TRUNK</interface-mode>
                                                        <trunk-vlans>100..110</trunk-vlans>
                                                </config>
                                        </switched-vlan>
                                </ethernet>
                        </interface>
                                {% endfor %}
                </interfaces>
        </config>
        '''
        intList = ['TenGigabitEthernet1/0/1','TenGigabitEthernet1/0/2','TenGigabitEthernet1/0/3']

        temp = Template(configChangesTemp)
        xmlConfigChanges = temp.render(intList=intList)
                
        editconfig = m.edit_config(target = 'candidate' ,config = xmlConfigChanges)
        print(editconfig)




        MyFilter ='''
        <filter>
        <interfaces xmlns="http://openconfig.net/yang/interfaces">
                        <interface>
                                <name>TenGigabitEthernet1/0/1</name>
                        </interface>
                        <interface>
                                <name>TenGigabitEthernet1/0/2</name>
                        </interface>
                        <interface>
                                <name>TenGigabitEthernet1/0/3</name>
                        </interface>
        </interfaces>
        </filter>
        '''

        runningConfig = m.get_config(source='running',filter=MyFilter).data_xml
        dom =  xml.dom.minidom.parseString(runningConfig) #or xml.dom.minidom.parse(c)
        pretty_xml_as_string = dom.toprettyxml()
        print(pretty_xml_as_string)
        print('#################################################################################')
        m.commit()

        MyFilter ='''
        <filter>
        <interfaces xmlns="http://openconfig.net/yang/interfaces">
                        <interface>
                                <name>TenGigabitEthernet1/0/1</name>
                        </interface>
                        <interface>
                                <name>TenGigabitEthernet1/0/2</name>
                        </interface>
                        <interface>
                                <name>TenGigabitEthernet1/0/3</name>
                        </interface>
        </interfaces>
        </filter>
        '''

        runningConfig = m.get_config(source='running',filter=MyFilter).data_xml
        dom =  xml.dom.minidom.parseString(runningConfig) #or xml.dom.minidom.parse(c)
        pretty_xml_as_string = dom.toprettyxml()
        print(pretty_xml_as_string)
