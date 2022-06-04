import time
from xml.etree import ElementTree


def get_network_usage(domain):
    net_in = ''
    net_out = ''
    tree = ElementTree.fromstring(domain.XMLDesc())
    interfaces = tree.findall('devices/interface/target')
    for i in interfaces:
        interface = i.get('dev')
        interface_info1 = domain.interfaceStats(interface)
        time.sleep(1)
        interface_info2 = domain.interfaceStats(interface)
        net_in = (interface_info2[0] - interface_info1[0]) / 1024
        net_out = (interface_info2[4] - interface_info1[4]) / 1024
        break
    return net_in, net_out
