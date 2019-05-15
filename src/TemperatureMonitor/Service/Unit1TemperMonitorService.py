#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/5/10 22:36'
from src.Config.Unit1GroupConfig import LowerWaterWall_1,UpperWaterWall_1,\
    HighTemperatureSuperheater45_Area_1
from src.TemperatureMonitor.Dao.DataHandleDao import TemperEstimate





def MonitorUnit1(opcData,CurveFunctions,presure,redisClient,fixedValueFunctions=[]):

    """
        壁温监控
    """
    #下部水冷壁
    TemperEstimate(
        opcData[LowerWaterWall_1], #opc数据
        fixedValueFunctions['LowerWaterWall'], #折线函数
        presure, #管内压力
        LowerWaterWall_1,#监控区域
        redisClient,
    )


    # # 上部水冷壁
    # TemperEstimate(
    #     opcData[UpperWaterWall_1],
    #     fixedValueFunctions['UpperWaterWall1'],
    #     presure,
    #     UpperWaterWall_1,
    # )
    # # 高温过热器45
    # TemperEstimate(
    #     opcData[HighTemperatureSuperheater45_Area_1],
    #     CurveFunctions['highTemperatureSuperheaterModle45'],
    #     presure,
    #     HighTemperatureSuperheater45_Area_1,
    # )



