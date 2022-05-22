from django.urls import path
from virtualMachineMonitoringSystemBackend.views import virtual_machine_views, server_views, common_view

urlpatterns = [
    path('getServerCpuUsage', server_views.get_server_cpu_usage, name='getServerCpuUsage'),
    path('getServerMemoryUsage', server_views.get_server_memory_usage, name='getServerMemoryUsage'),
    path('getServerDiskUsage', server_views.get_server_disk_usage, name='getServerDiskUsage'),
    path('getServerNetworkUsage', server_views.get_server_network_usage, name='getServerNetworkUsage'),
    path('getAllVirtualMachinesName', virtual_machine_views.get_all_virtual_machines_name,
         name='getAllVirtualMachinesName'),
    path('getAllRunningVirtualMachinesName', virtual_machine_views.get_all_running_virtual_machines_name,
         name='getAllRunningVirtualMachinesName'),
    path('getRunningVirtualMachinesCpuUsage', virtual_machine_views.get_running_virtual_machine_cpu_usage,
         name='getRunningVirtualMachinesCpuUsage'),
    path('getRunningVirtualMachinesMemoryUsage', virtual_machine_views.get_running_virtual_machine_memory_usage,
         name='getRunningVirtualMachinesMemoryUsage'),
    path('getRunningVirtualMachinesDiskUsage', virtual_machine_views.get_running_virtual_machine_disk_usage,
         name='getRunningVirtualMachinesDiskUsage'),
    path('getRunningVirtualMachinesNetworkUsage', virtual_machine_views.get_running_virtual_machine_network_usage,
         name='getRunningVirtualMachinesNetworkUsage'),
    path('checkConnection', common_view.check_connect, name='checkConnection'),
    path('addServer', common_view.add_server, name='addServer'),
    path('startGetData', common_view.start_get_data, name='startGetData'),
    path('deleteServer', common_view.delete_server, name='deleteServer'),
]
