#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""容器类"""

from inspect import isclass, isfunction


class App(object):
    _shares = {}  # 共享实例
    _alias = {  # 别名
        'redis': 'simutil.Redis.Redis',
        'log': 'simutil.Log.Log',
        'request': 'simutil.Request.Request',
        'env': 'simutil.Env.Env',
        'async': 'simutil.Async.Async',
        'config': 'simutil.ConfigParser.ConfigParser',
        'oss': 'simutil.Oss.Oss',
    }

    _share_instance = None

    # Env为单例模式
    def __new__(cls, *args, **kw):
        if not cls._share_instance:
            cls._share_instance = super(App, cls).__new__(cls, *args, **kw)
        return cls._share_instance

    def register(self, key, alias):
        '''
        注册方法
        :param key: 注册类是对应的key
        :param alias: 注册的字符转，实例或者类
        :return: None
        '''
        if self._shares.get(key):
            del self._shares[key]
        if isinstance(alias, str):
            self._alias[key] = alias
        elif isclass(alias) or isfunction(alias):  # 注册类 & function
            self._alias[key] = alias
        elif isinstance(alias.__class__.__class__, type):  # 注册实例 (这边判断是否是实例 不太严谨)
            self._shares[key] = alias
            self._alias[key] = alias.__class__
        else:  # 其他
            self._alias[key] = alias
        return self

    def _instance(self, name):
        '''
        获取新的实例
        :param name: 对应的name
        :return: instance
        '''
        alias = self._alias.get(name)
        if alias is None:
            raise Exception('create instance fail, for {} not register'.format(name))
        if type(alias) == str:
            self._shares[name] = self._instance_by_str(alias)
        elif isfunction(alias):
            pass
        elif isinstance(alias, type):
            self._shares[name] = alias()
        elif isinstance(alias.__class__.__class__, type):
            self._shares[name] = alias.__class__()
        return self._shares.get(name) or self._alias[name]

    def _instance_by_str(self, alias):
        '''
        通过字符串实例华
        :param name: 注册调用使用的名称
        :param path: 路径
        :return:
        '''
        import importlib
        try:
            Import = importlib.import_module('{}'.format('.'.join(alias.split('.')[:-1])))
            classname = getattr(Import, alias.split('.')[-1])
            if isinstance(classname, type):
                return classname()
            elif isinstance(classname.__class__.__class__, type):
                return classname.__class__()
        except Exception as e:
            return alias

    def __call__(self, name):
        return self._shares.get(name) or self._instance(name)


app = App()
