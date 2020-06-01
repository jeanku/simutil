#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pymysql
import codecs, os


class Artisan():
    author = 'jemes'                                            # 作者

    profix = 'lh_'                                              # 表前缀

    profix_filter = True                                        # 表前缀过滤 符合才生成model

    namespace = 'Models.Longhash'                               # 命名空间

    database = 'database'                                       # 数据库名称

    path = os.path.abspath(os.path.dirname(__file__))           # 当前路径

    output = None                                               # 输出路径

    config = {                                                  # 数据库配置
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'dev',
        'password': 'dev',
        'db': 'database',
        'charset': 'utf8mb4',
    }

    def handle(self, args=sys.argv):
        '''
        处理model入口方法
        :param args: 命令行输入参数
        :return:
        '''
        self.check(args)
        if args.__len__() == 2:                                 # 只有一个表名称
            modelname = self.auth_model_name(args[1])
        else:
            modelname = self.define_model_name(args[2])
        tablename = args[1]
        if tablename[:self.profix.__len__()] != self.profix and self.profix_filter:  # 表面前缀不一致 则不处理
            return
        sql = self.table_sql(tablename)
        self.model(modelname, tablename, sql)

    def all(self):
        '''
        处理model入口方法
        :param args: 命令行输入参数
        :return:
        '''
        tables = [index[0] for index in self.tables()]
        for index in tables:
            self.handle([None, index])
        self.basemodel()

    def check(self, args):
        '''
        校验配置是否正确
        :param args:
        :return:
        '''
        if args.__len__() == 1:
            raise Exception('invalid params')
        if self.config is None:
            raise Exception('databse not config')
        if self.output is None:
            raise Exception('output path invalid')

    def auth_model_name(self, tablename):
        '''
        根据表名自动生成model名称
        :param tablename: 表名称
        :return:
        '''
        if tablename[:self.profix.__len__()] != self.profix:  # 表面前缀不一致 则不处理
            tablename = tablename.replace('-', '_').split('_')
        else:
            tablename = tablename[self.profix.__len__():].replace('-', '_').split('_')
        return ''.join([index.capitalize() for index in tablename]) + 'Model'

    def define_model_name(self, name):
        '''
        生成用户自定义model名称
        :param name: model名称
        :return:
        '''
        return name.capitalize() if name[-5:] == 'Model' else name.capitalize() + 'Model'

    def tables(self):
        '''
        显示sql
        :param tablesname:
        :return:
        '''
        db = pymysql.connect(**self.config)
        cursor = db.cursor()
        cursor.execute("show tables")
        result = cursor.fetchall()
        db.close()
        return result

    def table_sql(self, tablesname):
        '''
        显示sql
        :param tablesname:
        :return:
        '''
        db = pymysql.connect(**self.config)
        cursor = db.cursor()
        cursor.execute("show full columns from `%s`" % tablesname)
        result = cursor.fetchall()
        db.close()
        return result

    def model(self, modelname, tablename, sql):
        '''
        生成model
        :param name: 生成的model名称
        :param tablename: 表名称
        :param sql: 表的结构
        :return:
        '''
        columns = [index[0] for index in sql]
        with codecs.open(self.path + '/model.txt', "rb", "UTF-8") as f:
            s = f.read()
        _template_parameter = {
            'author': self.author,
            'namespace': self.namespace,
            'classname': modelname,
            'database': self.database,
            'tablename': tablename,
            'columns': self.format_columns(sql),
            'create_time': '\'create_time\'' if 'create_time' in columns else None,
            'update_time': '\'update_time\'' if 'update_time' in columns else None
        }
        s = s % _template_parameter
        with codecs.open(self.output + '/' + modelname + '.py', "wb", "UTF-8") as f:
            f.write(s)
            f.flush()

    def format_columns(self, sql):
        '''
        生成column & 注释
        :param sql:
        :return:
        '''
        columns = [index[0] for index in sql]
        max_value = max([index.__len__() for index in columns])
        comments = [index[-1] for index in sql]
        data = ['\'{}\', {} # {}'.format(columns[i], ' ' * (50 + max_value - columns[i].__len__()), comments[i]) for i in range(columns.__len__())]
        return '\n        '.join(data)

    def basemodel(self):
        '''
        生成base model.txt
        :return:
        '''
        with codecs.open(self.path + '/basemodel.txt', "rb", "UTF-8") as f:
            s = f.read()
        with codecs.open(self.output + '/BaseModel.py', "wb", "UTF-8") as f:
            f.write(s)
            f.flush()


if __name__ == '__main__':
    sql = Artisan().handle([None, 'lh_test'])
    # sql = Artisan().all()
    # sql = Artisan().basemodel()
    pass
