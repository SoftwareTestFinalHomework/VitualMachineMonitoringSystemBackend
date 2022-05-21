import psutil
import time


def get_network_key():
    key_info = psutil.net_io_counters(pernic=True).keys()  # 获取网卡名称
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
