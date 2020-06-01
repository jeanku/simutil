#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Log日志类"""

__author__ = ''

import logging
import datetime
from .Env import Env
from pathlib import Path


class Log(object):
    _instance = {}  # 安日志存储logging 实例对象

    def debug(self, msg):
        self.logger().debug(self._format_msg(msg))

    def info(self, msg):
        self.logger().info(self._format_msg(msg))

    def warning(self, msg):
        self.logger().warning(self._format_msg(msg))

    def error(self, msg):
        self.logger().error(self._format_msg(msg))

    def critical(self, msg):
        self.logger().critical(self._format_msg(msg))

    def logger(self):
        date = datetime.datetime.now().strftime("%Y%m%d")
        if self._instance.get(date) is None:
            logger = logging.getLogger("logging")
            formatter = logging.Formatter('%(asctime)s 【%(levelname)s】%(message)s')
            logger.setLevel(Env()('LOG_LEVEL', 'DEBUG'))  # log level
            fh = logging.FileHandler(self._logfile())
            fh.setFormatter(formatter)
            if Env()('LOG_DEBUG', 'false').lower() == 'true':  # debug
                sh = logging.StreamHandler()
                sh.setFormatter(formatter)
                logger.addHandler(sh)
            logger.addHandler(fh)
            self._instance[date] = logger
        return self._instance.get(date)

    def _logfile(self):
        '''
        处理日志文件路径
        :return:
        '''
        date = datetime.datetime.now().strftime("%Y%m%d")
        path = Env()('LOG_PATH', None)
        if path is not None and path:
            path = Path(path)
            if path.is_dir():
                return path.joinpath('{}.log'.format(date))
            return path
        else:
            raise Exception('LOG_PATH not set in .env file')
        # return Path(Env.basedir).joinpath('Storage/Logs/{}.log'.format(date))  # 默认 ./Storage/Logs/**.log

    def _format_msg(self, msg):
        if isinstance(msg, BaseException):
            import traceback
            return traceback.format_exc()
        return msg.__str__()