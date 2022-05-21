from django.urls import path
from virtualMachineMonitoringSystemBackend.views import vitual_machine_views, server_views

urlpatterns = [
    path('getServerCpuUsage', server_views.get_server_cpu_usage, name='getServerCpuUsage'),
    path('getServerMemoryUsage', server_views.get_server_memory_usage, name='getServerMemoryUsage'),
    path('getServerDiskUsage', server_views.get_server_disk_usage, name='getServerDiskUsage'),
    path('getServerNetworkUsage', server_views.get_server_network_usage, name='getServerNetworkUsage')
]
