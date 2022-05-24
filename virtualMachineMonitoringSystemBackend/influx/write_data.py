import time
import libvirt
from influxdb import InfluxDBClient
import threading

from virtualMachineMonitoringSystemBackend.utils.cpu_utils import get_cpu_usage
from virtualMachineMonitoringSystemBackend.utils.disk_utils import get_disk_usage
from virtualMachineMonitoringSystemBackend.utils.memory_utils import get_memory_usage
from virtualMachineMonitoringSystemBackend.utils.network_utils import get_network_usage


# CREATE RETENTION POLICY "thirty_days" ON "machine_data" DURATION 30d REPLICATION 1 DEFAULT

# CREATE CONTINUOUS QUERY "cq_30m" ON "machine_data" BEGIN SELECT mean(ubuntu_01_usage) INTO
# "autogen".ubuntu_01_usage_30m FROM ubuntu_01_usage GROUP BY time(30m) END

# DROP CONTINUOUS QUERY ubuntu_01_30m ON machine_data

class WriteMachineData(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.conn = libvirt.open("qemu:///system")
        self.domain = self.conn.lookupByName(self.name)
        self.client = InfluxDBClient('localhost', 8086, database='machine_data')
        # client.create_retention_policy(name='thirty_days', duration='30d', replication='1', database='machine_data',
        #                                default=True)
        select = 'SELECT mean(cpu_usage),mean(memory_usage),mean(disk_usage),mean(network_out_usage),' \
                 'mean(network_in_usage) INTO "autogen".ubuntu_01_usage_30m FROM ubuntu_01_usage GROUP BY time(30m) '
        self.client.create_continuous_query(self.name + '_30m', select, 'machine_data')

    def run(self) -> None:
        while True:
            cpu_data = [
                {
                    "measurement": self.name + "_usage",
                    "fields": {
                        "cpu_usage": get_cpu_usage(self.domain, 1),
                        "memory_usage": get_memory_usage(self.domain, 1),
                        "disk_usage": get_disk_usage(self.domain),
                        "network_out_usage": get_network_usage(self.domain)[1],
                        "network_in_usage": get_network_usage(self.domain)[0]
                    }
                }
            ]
            time.sleep(3)
            self.client.write_points(cpu_data)

    def __del__(self):
        self.conn.close()
        self.client.close()


