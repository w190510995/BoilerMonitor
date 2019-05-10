#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/5/10 22:26'

from src.TemperatureMonitor.Service.Unit1TemperMonitorService import Monitor
from src.OpcHandle.Service.AreaRealDataServer import OpcAreaDataService



def MonitorAllUnit():
    """
    #1、#2机组壁温监控
    """
    ALLAreaData = OpcAreaDataService()  # 获得所有区域OPC数据
    Monitor(ALLAreaData)
    pass

if __name__ == '__main__':
    MonitorAllUnit()
    print()

