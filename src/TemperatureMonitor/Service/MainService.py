#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/5/10 22:30'

import  threading,time
from src.TemperatureMonitor.Service.TemperMoinitorSevice import MonitorAllUnit

"""
    #1、#2机组壁温、温差报警监控
"""

def StartThread():
    """
        开启线程，监控所需内容

    """
    #设置线程
    overTemp = threading.Thread(target=MonitorAllUnit) #壁温监控线程


    #开启线程
    overTemp.start()
