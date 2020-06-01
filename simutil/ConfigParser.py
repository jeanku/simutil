#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib


class ConfigParser(object):
    __loaded__ = dict()

    def __call__(self, module, default=None):
        module = module.split('.')
        key = '{}'.format('.'.join(module[:-1]))
        if self.__loaded__.get(key) is None:
            self.__loaded__[key] = importlib.import_module(key)
        return getattr(self.__loaded__[key], module[-1], default)

    def get(self, module, default=None):
        return self.__call__(module, default)


if __name__ == '__main__':
    data = ConfigParser()('Config.Filepath.RESOURCE_BASE_PATH')
    data = ConfigParser()('Config.Filepath.RESOURCE_BASE_PATH1', 'default')
    data = ConfigParser().get('Config.Filepath.RESOURCE_BASE_PATH')
    data = ConfigParser().get('Config.Settings.BLUR_MASK_MODIFIER', 'default')
    print(data)
