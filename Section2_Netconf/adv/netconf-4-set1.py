#https://blogs.cisco.com/developer/using-cli-as-training-wheels-with-netconfyang
#https://networkop.co.uk/blog/2017/01/25/netconf-intro/
#https://www.fir3net.com/Networking/Concepts-and-Terminology/how-to-configure-a-cisco-csr-using-netconf-yang.html
#https://www.fir3net.com/Networking/Protocols/how-to-operate-a-device-using-netconf-and-python.html
#https://github.com/ncclient/ncclient



from ncclient import manager
import xml.dom.minidom
import xmltodict
import xml.etree.ElementTree as ET


USERNAME = "cisco"
PASSWORD = "cisco"
HOST = '192.168.0.200'
m = manager.connect(host=HOST, port=830, username=USERNAME,
                    password=PASSWORD, device_params={'name': 'iosxe'})

m.connected

#print("######################################### m.get_schema(*) #############################################################")

schema = m.get_schema('ietf-ip')
root = ET.fromstring(schema.xml)
yang_text = list(root)[0].text
with open('ietf-ip.yang','w')as f:
    f.write(yang_text)


schema = m.get_schema('ietf-interfaces')
root = ET.fromstring(schema.xml)
yang_text = list(root)[0].text
with open('ietf-interfaces.yang','w')as f:
    f.write(yang_text)

schema = m.get_schema('ietf-inet-types')
root = ET.fromstring(schema.xml)
yang_text = list(root)[0].text
with open('ietf-inet-types.yang','w')as f:
    f.write(yang_text)


schema = m.get_schema('ietf-yang-types')
root = ET.fromstring(schema.xml)
yang_text = list(root)[0].text
with open('ietf-yang-types.yang','w')as f:
    f.write(yang_text)



#print('######################################### ET.fromstring(schema.xml) #############################################################')



schema = m.get_schema('ietf-ip')
root = ET.fromstring(schema.xml)
yang_text = list(root)[0].text
with open('openconfig-extensions.yang','w')as f:
    f.write(yang_text)


schema = m.get_schema('openconfig-interfaces')
root = ET.fromstring(schema.xml)
yang_text = list(root)[0].text
with open('openconfig-interfaces.yang','w')as f:
    f.write(yang_text)

schema = m.get_schema('openconfig-yang-types')
root = ET.fromstring(schema.xml)
yang_text = list(root)[0].text
with open('openconfig-yang-types.yang','w')as f:
    f.write(yang_text)


schema = m.get_schema('openconfig-types')
root = ET.fromstring(schema.xml)
yang_text = list(root)[0].text
with open('openconfig-types.yang','w')as f:
    f.write(yang_text)



m.close_session()
