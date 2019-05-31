#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/5/31 20:59'
from src.Config.TagGroupConfig import MainSteamPressure, \
    HighTempReheaterSteam,LowTempReheatSteam,LowerWaterWall,UpperWaterWall,\
    EconomizerExport,ProofExport,HorizontalFlueSideWall,RearShaftWallTube38,\
    RearShaftWallTube51,LowTemperatureSuperheater,PlatenSuperheater45,\
    PlatenSuperheater51,HighTemperatureSuperheater45,HighTemperatureSuperheater51,\
    LowTemperatureReheater,HighTemperatureReheater


#
# def GetSteamPressure(opcData,unit='1'):
#
#
#     # 选择后锅炉主蒸汽压力
#     MainSteam = opcData[MainSteamPressure+'_'+unit]
#     # 选择后锅炉主蒸汽压力
#     HighTemperatureReheaterSteam = opcData[HighTempReheaterSteam +'_'+unit]
#     #低温再热器进口联箱左侧进口压力(含左右侧两个点)
#     LowTempReheaterSteam = opcData[LowTempReheatSteam+'_'+unit]
#     pr1 =
#
#     return {
#         LowerWaterWall:20,
#         UpperWaterWall:20,#固定定值，与压力无关，随便什么值都可以
#         EconomizerExport
#     }
