from ncclient import manager


USERNAME = "cisco"
PASSWORD = "cisco"
HOST = '192.168.0.222'
m = manager.connect(host=HOST, port=830, username=USERNAME,
                    password=PASSWORD, device_params={'name': 'iosxe'})



with open('/home/carl/Dropbox/NetworkAutomationTraining/Other/~Netconf/new_interface.xml') as f:
    xml = f.read()

reply = m.edit_config(target='running', config=xml)
print("Success? {}".format(reply.ok))
m.close_session()
