from influxdb import InfluxDBClient


class GetMachineData:
    def __init__(self, name):
        self.name = name
        self.client = InfluxDBClient('localhost', 8086, database='machine_data')

    def get_data_five_minutes_ago(self):
        points = self.client.query('select * from ' + self.name + '_usage order by time desc limit 50').get_points()
        return list(points)

    def get_data_thirty_minutes_interval(self):
        points = self.client.query('select * from autogen.' + self.name + '_usage_30m').get_points()
        return list(points)

    def __del__(self):
        self.client.close()


if __name__ == '__main__':
    # GetMachineData('ubuntu_01').get_data_five_minutes_ago()
    GetMachineData('ubuntu_01').get_data_thirty_minutes_interval()
