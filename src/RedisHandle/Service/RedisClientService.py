#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/5/15 16:41'

from src.Config.RedisConfg import Redis_port,Redis_host,Redis_pwd,Redis_db
import  redis
from src.OpcHandle.Dao.DataByte2Str import convert

import pandas as pd


def RedisClient():
    pool = redis.ConnectionPool(host = Redis_host,port = Redis_port,password=Redis_pwd,db=Redis_db)
    client = redis.Redis(connection_pool=pool)
    redis.StrictRedis(host=Redis_host, port=Redis_port, password=Redis_pwd,db=Redis_db)
    return  client



if __name__ == '__main__':

    client = RedisClient()
    data = client.hgetall('10HAD16CT240')
    # data = convert(data)

    # data = str(data,encoding='utf-8')

    print(data['maxValue'])

