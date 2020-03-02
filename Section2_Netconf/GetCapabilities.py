
from ncclient import manager
import xml.dom.minidom
import xmltodict

Host = '192.168.0.200'
Port = 830
User = 'cisco'
Pass = 'cisco'

netconf_connection = manager.connect(host = Host,
                                    port = Port,
                                    username=User,
                                    password=Pass,
                                    hostkey_verify=False,
                                    timeout= 200, 
                                    allow_agent=False,
                                    look_for_keys=False,
                                    )


print(netconf_connection)

print('########################### client_capabilities ################################')

for i in netconf_connection.client_capabilities:
    print(i)

print('########################### server_capabilities ################################')
for i in netconf_connection.server_capabilities:
    print(i)



netconf_connection.close_session()

