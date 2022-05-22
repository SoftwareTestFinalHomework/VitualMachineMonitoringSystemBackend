import psutil
import time
from xml.etree import ElementTree


def get_network_key():
    key_info = psutil.net_io_counters(pernic=True).keys()
    recv = {}
    sent = {}
    for key in key_info:
        recv.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)
        sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)

    return key_info, recv, sent


def get_network_rate():
    key_info, old_recv, old_sent = get_network_key()
    time.sleep(1)
    key_info, now_recv, now_sent = get_network_key()
    net_in = {}
    net_out = {}
    for key in key_info:
        net_in.setdefault(key, (now_recv.get(key) - old_recv.get(key)) / 1024)
        net_out.setdefault(key, (now_sent.get(key) - old_sent.get(key)) / 1024)

    return key_info, net_in, net_out


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
