# VitualMachineMonitoringSystemBackend
使用Python Django搭建的虚拟机数据监控后端服务

##### 小组成员

| 小组成员 | 学号    |
| -------- | ------- |
| 李航宇   | 1913092 |
| 高鹏     | 1913073 |
| 马宁     | 1913780 |
| 郭书奇   | 1812985 |

##### 部署方式

###### 服务器环境依赖安装(Ubuntu)

```shell
sudo apt-get install libvirt 
sudo apt-get install qemu
sudo apt-get install virt-manager
systemctl start libvirtd
systemctl enable libvirtd
```

###### 启动Django项目(安装libvirt-python时虚拟环境可能会报错，如遇到此问题看之后的解决方案)

```shell
git clone git@github.com:SoftwareTestFinalHomework/VitualMachineMonitoringSystemBackend.git
cd VitualMachineMonitoringSystemBackend

# 创建Python虚拟环境
sudo pip install virtualenv
virtualenv venv
# 激活虚拟环境
source ./venv/bin/activate
pip install -r requirements.txt

# 启动Django项目
python manage.py runserver 0.0.0.0:8000
```

> 安装libvirt-python时虚拟环境报错解决方法

```shell
sudo pip install libvirt-python # 在全局环境中安装libvirt-python
virtualenv venv --system-site-packages # 使虚拟环境可以使用全局环境中的packages
```



##### 网络请求接口

| 网络请求 | /getAllVirtualMachinesName     |
| -------- | ------------------------------ |
| 请求类型 | GET                            |
| 请求参数 | None                           |
| 含义     | 获取该服务器上所有虚拟机的名称 |

响应格式

```json
{
    "allVirtualMachines": [
        "lhy",
        "test",
        "unbuntu_command",
        "ubuntu_01"
    ]
}
```



| 网络请求 | /getAllRunningVirtualMachinesName      |
| -------- | -------------------------------------- |
| 请求类型 | GET                                    |
| 请求参数 | None                                   |
| 含义     | 获取该服务器上所有运行中的虚拟机的名称 |

响应格式

```json
{
    "allRunningVirtualMachines": [
        "unbuntu_command",
        "ubuntu_01"
    ]
}
```



| 网络请求 | /getRunningVirtualMachinesCpuUsage        |
| -------- | ----------------------------------------- |
| 请求类型 | GET                                       |
| 请求参数 | name(虚拟机名称)                          |
| 含义     | 获取该服务器上指定名称的虚拟机的cpu使用率 |

响应格式

```json
{
    "cpu_usage": 2.291225908463071
}
```





| 网络请求 | /getRunningVirtualMachinesMemoryUsage      |
| -------- | ------------------------------------------ |
| 请求类型 | GET                                        |
| 请求参数 | name(虚拟机名称)                           |
| 含义     | 获取该服务器上指定名称的虚拟机的内存使用率 |

响应格式

```json
{
    "memory_usage": 90.88503653304059
}
```



| 网络请求 | /getRunningVirtualMachinesDiskUsage        |
| -------- | ------------------------------------------ |
| 请求类型 | GET                                        |
| 请求参数 | name(虚拟机名称)                           |
| 含义     | 获取该服务器上指定名称的虚拟机的磁盘使用率 |

响应格式

```json
{
    "disk_usage": 0.5203060913085937
}
```



| 网络请求 | /getRunningVirtualMachinesNetworkUsage       |
| -------- | -------------------------------------------- |
| 请求类型 | GET                                          |
| 请求参数 | name(虚拟机名称)                             |
| 含义     | 获取该服务器上指定名称的虚拟机的网络使用情况 |

响应格式

```json
{
    "net_in": 0.05078125,
    "net_out": 0.0
}
```



| 网络请求 | /checkConnection                 |
| -------- | -------------------------------- |
| 请求类型 | GET                              |
| 请求参数 | None                             |
| 含义     | 检查服务器上的Django服务是否正常 |

响应格式

```json
{
    "status": "success"
}
```



| 网络请求 | /addServer                                       |
| -------- | ------------------------------------------------ |
| 请求类型 | GET                                              |
| 请求参数 | ip(对应服务器的IP地址)                           |
| 含义     | 将对应的服务器信息添加到能够服务的配置文件列表中 |

响应格式

```json
{
    "status": "success"
}
```



| 网络请求 | /startGetData                                                |
| -------- | ------------------------------------------------------------ |
| 请求类型 | GET                                                          |
| 请求参数 | name(虚拟机名称)                                             |
| 含义     | 启动一个新的线程将虚拟机的各种(CPU利用率，内存利用率，磁盘利用率，网络速率)数据写入到influxDB中 |

响应格式

```json
{
    "status": "success"
}
```



| 网络请求 | /deleteServer                              |
| -------- | ------------------------------------------ |
| 请求类型 | GET                                        |
| 请求参数 | ip(对应服务器的IP地址)                     |
| 含义     | 将指定的服务器从Django服务的配置列表中删除 |

响应格式

```json
{
    "status": "success"
}
```



| 网络请求 | /getSelectedVirtualMachineData       |
| -------- | ------------------------------------ |
| 请求类型 | GET                                  |
| 请求参数 | name(虚拟机名称)，interval(时间间隔) |
| 含义     | 从influxDB中获取指定虚拟机的数据     |

响应格式

```json
{
    "data": [
        {
            "time": "2022-06-03T06:59:43.352996Z",
            "cpu_usage": 1.808361645493397,
            "disk_usage": 0.5203060913085937,
            "memory_usage": 90.88503653304059,
            "network_in_usage": 0.0,
            "network_out_usage": 0.0
        },
        {
            "time": "2022-06-03T06:59:37.301908Z",
            "cpu_usage": 2.038658697431247,
            "disk_usage": 0.5203060913085937,
            "memory_usage": 90.87860253579916,
            "network_in_usage": 0.0,
            "network_out_usage": 0.0
        },
        .........
    ]
}
```



| 网络请求 | /createNewVirtualMachine                                     |
| -------- | ------------------------------------------------------------ |
| 请求类型 | POST                                                         |
| 请求参数 | cpuNum, memorySize, diskSize, osTypeSelected, virtualMachineName |
| 含义     | 在服务器上创建一个新的虚拟机                                 |

响应格式

```json
{
    "status": "success"
}
```



| 网络请求 | /deleteVirtualMachine        |
| -------- | ---------------------------- |
| 请求类型 | POST                         |
| 请求参数 | virtualMachineName           |
| 含义     | 在服务器上删除掉指定的虚拟机 |

响应格式

```json
{
    "status": "success"
}
```

