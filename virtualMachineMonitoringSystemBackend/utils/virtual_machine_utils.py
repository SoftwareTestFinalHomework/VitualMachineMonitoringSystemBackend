import subprocess

from virtualMachineMonitoringSystemBackend.influx.write_data import WriteMachineData


def create_virtual_machine(cpu_num, memory_size, disk_size, os_type_selected, virtual_machine_name):
    memory_size = memory_size * 1024
    disk_size = disk_size
    iso_path = ''
    if os_type_selected == 'Ubuntu22.04':
        iso_path = '../../ubuntu-22.04-desktop-amd64.iso'
    elif os_type_selected == 'Ubuntu20.04':
        iso_path = '../../ubuntu-20.04.4-desktop-amd64.iso'
    elif os_type_selected == 'Ubuntu18.04':
        iso_path = '../../ubuntu-18.04.6-desktop-amd64.iso'

    command = 'virt-install --virt-type kvm --vcpus={cpu_num} --name {virtual_machine_name} --ram {memory_size} ' \
              '--cdrom {iso_path} --disk path=/var/lib/libvirt/images/{virtual_machine_name}.img,size={disk_size},' \
              'format=qcow2,bus=virtio --os-type=linux --network=default --graphics vnc' \
        .format(cpu_num=cpu_num, iso_path=iso_path, memory_size=memory_size, disk_size=disk_size,
                virtual_machine_name=virtual_machine_name)
    print(command)
    subprocess.Popen("echo '123' | sudo -S " + command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    WriteMachineData(virtual_machine_name)


if __name__ == '__main__':
    create_virtual_machine(1, 1, 20, 'Ubuntu20.04', 'test2')
