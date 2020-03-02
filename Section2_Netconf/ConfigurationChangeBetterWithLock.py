
from ncclient import manager
import xml.dom.minidom
import xmltodict
from ncclient import manager, xml_
import time

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


        with m.locked('running'):
                time.sleep(30)
                configChanges = '''
                <config>
                <interfaces xmlns="http://openconfig.net/yang/interfaces">
                                <interface>
                                        <name xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">{intName}</name>
                                        <ethernet xmlns="http://openconfig.net/yang/interfaces/ethernet">
                                                <switched-vlan xmlns="http://openconfig.net/yang/vlan">
                                                        <config>
                                                                <interface-mode>ACCESS</interface-mode>
                                                                <access-vlan>{access_Vlan}</access-vlan>
                                                        </config>
                                                </switched-vlan>
                                        </ethernet>
                                </interface>
                        </interfaces>
                </config>
                '''
                InterfaceName = 'TenGigabitEthernet1/0/4'

                configChanges = configChanges.format(intName = InterfaceName , access_Vlan = '10')
                #print(configChanges)
                editconfig = m.edit_config(target = 'running' ,config = configChanges)
                print(editconfig)

                save_body = """
                <cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>
                """
                netconf_reply = m.dispatch(xml_.to_ele(save_body))
                filterXml = '''
                <filter>
                <interfaces xmlns="http://openconfig.net/yang/interfaces">
                                <interface>
                                        <name>{intName}</name>
                                </interface>
                        </interfaces>
                </filter>
                '''
                filterXml = filterXml.format(intName = InterfaceName)
                runningConfig = m.get_config(source='running',filter=filterXml).data_xml
                dom =  xml.dom.minidom.parseString(runningConfig) #or xml.dom.minidom.parse(c)
                pretty_xml_as_string = dom.toprettyxml()
                print(pretty_xml_as_string)
