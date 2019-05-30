#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/5/10 22:00'
from src.OpcHandle.Dao.GetOpcDataDao import GetDataFromOpc


def OpcAreaDataService():
    """
    提供各区域壁温数据
    :return:
    """
    opcData = GetDataFromOpc()

    return opcData

if __name__ == '__main__':
    data = OpcAreaDataService()
    print()

