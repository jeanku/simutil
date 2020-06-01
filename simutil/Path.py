#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Path类"""

__author__ = ''

from pathlib import Path as BasePath
from simutil.App import app


class Path():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = BasePath(app('BASE_PATH'))
        return cls._instance
