import json
from django.http import JsonResponse
import libvirt

from virtualMachineMonitoringSystemBackend.influx.get_data import GetMachineData
from virtualMachineMonitoringSystemBackend.utils.cpu_utils import get_cpu_usage
from virtualMachineMonitoringSystemBackend.utils.disk_utils import get_disk_usage
from virtualMachineMonitoringSystemBackend.utils.memory_utils import get_memory_usage
from virtualMachineMonitoringSystemBackend.utils.network_utils import get_network_usage
from virtualMachineMonitoringSystemBackend.utils.virtual_machine_utils import create_virtual_machine, \
    delete_virtual_machine, create_virtual_machine_by_kscfg


def get_all_virtual_machines_name(request):
    conn = libvirt.open("qemu:///system")
    all_virtual_machines = []
    for domain in conn.listAllDomains():
        all_virtual_machines.append(domain.name())
    conn.close()
    return JsonResponse({
        'allVirtualMachines': all_virtual_machines
    })


def get_all_running_virtual_machines_name(request):
    conn = libvirt.open("qemu:///system")
    all_running_virtual_machines = []
    for vid in conn.listDomainsID():
        domain = conn.lookupByID(vid)
        all_running_virtual_machines.append(domain.name())
    conn.close()
    return JsonResponse({
        'allRunningVirtualMachines': all_running_virtual_machines
    })


def get_running_virtual_machine_cpu_usage(request):
    cpu_usage = ''
    if request.method == 'GET':
        conn = libvirt.open("qemu:///system")
        domain = conn.lookupByName(request.GET['name'])
        cpu_usage = get_cpu_usage(domain, 1)
        conn.close()
        return JsonResponse({
            'cpu_usage': cpu_usage
        })
    return JsonResponse({
        'errMsg': 'method must be GET'
    })


def get_running_virtual_machine_memory_usage(request):
    memory_usage = ''
    if request.method == 'GET':
        conn = libvirt.open("qemu:///system")
        domain = conn.lookupByName(request.GET['name'])
        memory_usage = get_memory_usage(domain, 5)
        conn.close()
        return JsonResponse({
            'memory_usage': memory_usage
        })

    return JsonResponse({
        'errMsg': 'method must be GET'
    })


def get_running_virtual_machine_disk_usage(request):
    if request.method == 'GET':
        conn = libvirt.open("qemu:///system")
        domain = conn.lookupByName(request.GET['name'])
        disk_usage = get_disk_usage(domain)
        conn.close()
        return JsonResponse({
            'disk_usage': disk_usage
        })

    return JsonResponse({
        'errMsg': 'error'
    })


def get_running_virtual_machine_network_usage(request):
    if request.method == 'GET':
        conn = libvirt.open("qemu:///system")
        domain = conn.lookupByName(request.GET['name'])
        net_in, net_out = get_network_usage(domain)
        return JsonResponse({
            'net_in': net_in,
            'net_out': net_out
        })

    return JsonResponse({
        'errMsg': 'error'
    })


def get_selected_virtual_machine_data(request):
    result = []
    if request.method == 'GET':
        if request.GET['interval'] == '5s':
            result = GetMachineData(request.GET['name']).get_data_five_minutes_ago()
        elif request.GET['interval'] == '30m':
            result = GetMachineData(request.GET['name']).get_data_thirty_minutes_interval()

    return JsonResponse({
        'data': result
    })


def create_new_virtual_machine(request):
    data = json.loads(request.body)
    create_virtual_machine(data.get('cpuNum'), data.get('memorySize'), data.get('diskSize'), data.get('osTypeSelected'),
                           data.get('virtualMachineName'))
    return JsonResponse({
        'stat': 'success'
    })


def create_new_virtual_machine_by_kscfg(request):
    data = json.loads(request.body)
    create_virtual_machine_by_kscfg(data.get('cpuNum'), data.get('memorySize'), data.get('diskSize'),
                                    data.get('osTypeSelected'), data.get('virtualMachineName'))
    return JsonResponse({
        'stat': 'success'
    })


def delete_virtual_machine_by_name(request):
    data = json.loads(request.body)
    delete_virtual_machine(data.get('virtualMachineName'))
    return JsonResponse({
        'stat': 'success'
    })
