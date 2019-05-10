#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/5/10 22:36'
from src.Config.Unit1GroupConfig import LowerWaterWall_1,UpperWaterWall_1,\
    HighTemperatureSuperheater45_Area_1



"""
    #1机组壁温监控
"""

def Monitor(opcData):
    LowerWaterWall_data = opcData[LowerWaterWall_1]
    UpperWaterWall_data = opcData[UpperWaterWall_1]
    HighTemperatureSuperheater45_data = opcData[HighTemperatureSuperheater45_Area_1]
    print()



