#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""redis数据访问类"""

import redis
from .Env import Env


class Redis():
    _instance = dict()

    def __init__(self, host=None, port=6379, password=None, db=0):
        '''
        构造方法
        :param host: host
        :param port: port
        :param password: 密码
        :param db: 默认db
        '''
        env = Env()
        if host is not None:
            self.host = host
            self.port = port
            self.password = password
            self.db = db
        else:
            self.host = env("REDIS_HOST", 'localhost')
            self.port = int(env("REDIS_PORT", 6379))
            self.password = env('REDIS_PASSWORD', None)
            self.db = int(env("REDIS_DB", 0))

        if self._instance.get(self.db) is None:
            pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db, password=self.password, decode_responses=True)
            self._instance[self.db] = redis.Redis(connection_pool=pool)

    def select(self, db):
        '''
        切换redis库
        :param db: 库index
        :return: redis.Redis
        '''
        if type(db) != int:
            raise Exception('select db must be the type of int')
        if self._instance.get(db) is None:
            pool = redis.ConnectionPool(host=self.host, port=self.port, db=db, password=self.password, decode_responses=True)
            self._instance[db] = redis.Redis(connection_pool=pool)
        return self._instance[db]

    def __getattr__(self, key):
        '''
        默认库则调用
        :param key: redis 执行方法
        :return: result
        '''
        return self._instance.get(self.db).__getattribute__(key)

