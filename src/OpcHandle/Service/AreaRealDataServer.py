#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/5/10 22:00'
from src.OpcHandle.Dao.GetOpcDataDao import GetDataFromOpc
from src.Config.TagGroupConfig import MainSteamPressure, \
    HighTempReheaterSteam,LowTempReheatSteam,LowerWaterWall,UpperWaterWall

def OpcAreaDataService():
    """
    提供各区域壁温数据
    :return:
    """
    opcData = GetDataFromOpc()

    return opcData

if __name__ == '__main__':
    data = OpcAreaDataService()
    data2 = data[LowTempReheatSteam+'_1']
    f1 = float(data[LowTempReheatSteam+'_1'][0][1])
    f2 = float(data[LowTempReheatSteam+'_1'][1][1])

    print(type(float(f1)))

