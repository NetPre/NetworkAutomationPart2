



import pyeapi
from pprint import pprint as pp
pyeapi.load_config('/home/carl/Desktop/USBNetworkAutomation-Part2/Api/.eapi.conf')
node = pyeapi.connect_to('veos01')

lldpNeighbors = node.enable('show lldp neighbors')[0]['result']['lldpNeighbors']

for i in lldpNeighbors:
    print(i)
    print(node.config(['interface '+i['port'] , 'description connected to '+i['neighborDevice']+' on interface '+i['neighborPort']]))



