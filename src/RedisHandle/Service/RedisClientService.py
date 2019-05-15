#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/5/15 16:41'

from src.Config.RedisConfg import Redis_port,Redis_host,Redis_pwd,Redis_db
import  redis

def RedisClient():
    pool = redis.ConnectionPool(host = Redis_host,port = Redis_port,password=Redis_pwd,db=Redis_db)
    client = redis.Redis(connection_pool=pool)
    return  client



if __name__ == '__main__':
    client = RedisClient()
    client.hmset(
        'key1',{
            "tagname":'10HAD1232',
            'tagValue':123,
            'desc':'hhhhhh'
        }
    )
    data = client.hmget('key1',['tagname','tagValue','desc'])
    print(data)
