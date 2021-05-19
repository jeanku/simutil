#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""redis数据访问类"""

import pika
from .Env import Env


class RabbitMQ:
    _connection = None

    def __init__(self):
        '''
        构造方法
        :param host: host
        :param port: port
        :param password: 密码
        :param db: 默认db
        '''
        env = Env()
        credentials = pika.PlainCredentials(env('RABBITMQ_USER', ''), env('RABBITMQ_PASSWORD', ''))  # mq用户名和密码
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=env("RABBITMQ_HOST", 'localhost'), port=int(env("RABBITMQ_PORT", 5672)),
                                      credentials=credentials)
        )

    def channel(self) -> pika.adapters.blocking_connection.BlockingChannel.__class__:
        return self._connection.channel()

    def connection(self) -> pika.adapters.blocking_connection.BlockingConnection.__class__:
        return self._connection

