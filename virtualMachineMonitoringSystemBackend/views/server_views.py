from django.http import JsonResponse
import psutil
from virtualMachineMonitoringSystemBackend.utils.network_utils import get_network_rate


def get_server_cpu_usage(request):
    cpu_usage = psutil.cpu_percent(interval=1, percpu=False)
    return JsonResponse({
        'cpu_usage': cpu_usage
    })


def get_server_memory_usage(request):
    memory_info = psutil.virtual_memory()
    return JsonResponse({
        'memory_usage': memory_info.percent
    })


def get_server_disk_usage(request):
    disk_info = psutil.disk_usage('/')
    return JsonResponse({
        'disk_usage': disk_info.percent
    })


def get_server_network_usage(request):
    # KB
    key_info, net_in, net_out = get_network_rate()
    return JsonResponse({
        'net_in': net_in,
        'net_out': net_out
    })
