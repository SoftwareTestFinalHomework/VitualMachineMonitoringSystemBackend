from django.urls import path
from virtualMachineMonitoringSystemBackend.views import virtual_machine_views, common_view

urlpatterns = [
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
    path('getSelectedVirtualMachineData', virtual_machine_views.get_selected_virtual_machine_data,
         name='getSelectedVirtualMachineData'),
    path('createNewVirtualMachine', virtual_machine_views.create_new_virtual_machine_by_kscfg,
         name='createNewVirtualMachine'),
    path('deleteVirtualMachine', virtual_machine_views.delete_virtual_machine_by_name, name='deleteVirtualMachine'),
]
