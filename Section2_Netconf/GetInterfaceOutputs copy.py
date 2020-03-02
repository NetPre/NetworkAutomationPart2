
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
    <cpu-usage xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-process-cpu-oper">
    </cpu-usage>
    </filter>
    '''


    runningConfig = m.get(filter=MyFilter).data_xml
    dom =  xml.dom.minidom.parseString(runningConfig) #or xml.dom.minidom.parse(c)
    pretty_xml_as_string = dom.toprettyxml()
    print(pretty_xml_as_string)


    cpuLastFive = xmltodict.parse(pretty_xml_as_string)
    cpuLastFive = cpuLastFive['data']['cpu-usage']['cpu-utilization']['five-seconds']
    import json
    print(json.dumps(cpuLastFive, indent=2))