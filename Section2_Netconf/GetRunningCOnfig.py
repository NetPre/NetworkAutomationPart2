
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





    runningConfig = m.get_config(source='running').data_xml
    dom =  xml.dom.minidom.parseString(runningConfig) #or xml.dom.minidom.parse(c)
    pretty_xml_as_string = dom.toprettyxml()
    #print(pretty_xml_as_string)

with open('xmlRunningConfig.txt','w') as f:
    f.write(pretty_xml_as_string)


