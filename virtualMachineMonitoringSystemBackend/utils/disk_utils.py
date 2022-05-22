from xml.etree import ElementTree
import libvirt


def get_disk_usage(domain):
    disk_usage = -1
    tree = ElementTree.fromstring(domain.XMLDesc())
    devices = tree.findall('devices/disk/target')
    device_info = -1
    for d in devices:
        device = d.get('dev')
        if device == 'vda':
            try:
                device_info = domain.blockInfo(device)
            except libvirt.libvirtError:
                pass
            disk_usage = device_info[1] / device_info[0]
            break

    return disk_usage
