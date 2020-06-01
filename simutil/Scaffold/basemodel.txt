#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Util.Env import env
from simpysql.DBModel import DBModel


class BaseModel(DBModel):
    __basepath__ = env.base_path                    # 项目根目录



