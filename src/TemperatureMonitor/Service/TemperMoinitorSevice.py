#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/5/10 22:26'

from src.TemperatureMonitor.Service.TempMonConfigService import OverTemperatureMonitor
from src.OpcHandle.Service.AreaRealDataServer import OpcAreaDataService
from src.Model.Service.ModInitService import TempModelInit
from src.Model.Service.FixedValueServerce import LowerWaterWallModle,UpperWaterWallModle
from src.RedisHandle.Service.RedisClientService import RedisClient
from src.Config.TagGroupConfig import LowerWaterWall,UpperWaterWall
from src.Config.ThreadConfig import OverTempCycl
import time


def MonitorAllUnit():
    """
    #1、#2机组壁温监控
    """
    redisClient = RedisClient()
    CurveFunctions = TempModelInit()  #各个区域，动态报警定值生成折线函数

    FixedValueFunctions ={ #固定定值函数
        LowerWaterWall:LowerWaterWallModle,
        UpperWaterWall:UpperWaterWallModle,
    }


    #开启监视内容
    while True:
        ALLAreaData = OpcAreaDataService()  # 获得所有区域OPC数据
        OverTemperatureMonitor(ALLAreaData,CurveFunctions,20,redisClient,FixedValueFunctions)
        time.sleep(OverTempCycl) #扫描间隔


