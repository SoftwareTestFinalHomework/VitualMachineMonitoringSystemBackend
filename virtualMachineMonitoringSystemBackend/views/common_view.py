from django.http import JsonResponse

from virtualMachineMonitoringSystemBackend.config.server_config import servers
from virtualMachineMonitoringSystemBackend.influx.get_data import GetMachineData


def check_connect(request):
    return JsonResponse({
        'status': 'success'
    })


def add_server(request):
    if request.method == 'GET':
        servers.append(request.GET['ip'])
    return JsonResponse({
        'status': 'success'
    })


def start_get_data(request):
    if request.method == 'GET':
        GetMachineData(request.GET['name']).start()
        return JsonResponse({
            'status': 'success'
        })
