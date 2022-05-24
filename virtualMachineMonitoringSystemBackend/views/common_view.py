from django.http import JsonResponse

from virtualMachineMonitoringSystemBackend.config.server_config import servers
from virtualMachineMonitoringSystemBackend.influx.write_data import WriteMachineData


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


def delete_server(request):
    if request.method == 'GET':
        for i in range(len(servers)):
            if servers[i] == request.GET['ip']:
                servers.pop(i)
                break

    return JsonResponse({
        'status': 'success'
    })


def start_get_data(request):
    if request.method == 'GET':
        WriteMachineData(request.GET['name']).start()
        return JsonResponse({
            'status': 'success'
        })
