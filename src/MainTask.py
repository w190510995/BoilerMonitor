#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/5/30 10:20'
from src.TemperatureMonitor.Service.TemperMoinitorSevice import MonitorAllUnit


def StartMonitor():
    """
    开启所有服务
    """
    MonitorAllUnit()
