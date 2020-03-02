

#
# https://eos.arista.com/introducing-the-python-client-for-eapi-pyeapi/
# defalt host file is located at  ~/.eapi.conf to change use 
# pyeapi.load_config('/home/carl/Dropbox/NetworkAutomationTraining/Section10-API/API/.eapi.conf')
# https://eos.arista.com/working-with-the-python-eapi-client/
#


import pyeapi
from pprint import pprint as pp
pyeapi.load_config('/home/carl/Desktop/USBNetworkAutomation-Part2/Api/.eapi.conf')

node = pyeapi.connect_to('veos01')
pp(node.enable('show version'))


pp(node.config(['interface loopback 10','ip address 10.10.11.111/32']))


connection_2 = pyeapi.connect(transport='https', host='192.168.122.196', username='arista',
password='arista', return_node=True)


#pp(connection_2.execute('show version'))


pp(connection_2.enable('show version'))



