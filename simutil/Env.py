#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""环境变量类"""

__author__ = ''

from configparser import ConfigParser
from pathlib import Path
from .App import App

class Env():
    """Env主要是为了获取.env中的配置数据"""

    _instance = None

    _config = None

    _config_parser = None

    basedir = None

    # Env为单例模式
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Env, cls).__new__(cls, *args, **kw)
            cls._config_parser = MyConfigParser()
            cls._config_parser.read(Path(App()('BASE_PATH')).joinpath('.env'))
            cls._config = dict(cls._config_parser.items('environment'))
        return cls._instance

    def __call__(self, name, defaule=''):
        return self._config.get(name, defaule)

    def __getattr__(self, name):
        return self._config.get(name)

    def __getitem__(self, key):
        return self._config.get(key)

    def items(self, section, key=None, default=None):
        if key is None:
            return dict(self._config_parser.items(section))
        return dict(self._config_parser.items(section)).get(key, default)


class MyConfigParser(ConfigParser):
    """解决ConfigParser会将key名转成小写的问题"""

    def optionxform(self, str):
        return str


if __name__ == '__main__':
    import os
    App().register("BASE_PATH", os.path.dirname(os.path.dirname(__file__)))
    env = Env()
    print(env('LOG_PATH'))
    print(env('LOG_PATH1', "hahaha"))
    print(env.LOG_PATH)
    print(env['LOG_PATH'])
    print(env.items('sqlserver'))
    print(env.items('sqlserver', 'DB_HOST'))
    print(env.items('sqlserver', 'DB_HOST1', "123"))
