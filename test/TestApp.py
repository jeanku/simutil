from simutil.App import app, App
import os

if __name__ == '__main__':
    pass
    App().register("BASE_PATH", str(os.path.dirname(os.path.dirname(__file__))))

    # 环境初始化
    # Env
    # print(app('env')('LOG_PATH'))
    # print(app('env')('LOG_PATH1', "hahaha"))
    # print(app('env').LOG_PATH)
    # print(app('env')['LOG_PATH'])
    # print(app('env').items('sqlserver'))
    # print(app('env').items('sqlserver', 'DB_HOST'))
    # print(app('env').items('sqlserver', 'DB_HOST1', "123"))

    # Log
    # app('log').warning("123444")
    # app('log').info([1, 2, 3, 4, 5])
    # app('log').error({'name':'jemes'})
    # app('log').debug(("status", 0))
    # app('log').critical(5)
    # try:
    #     a = 100 / 0                                       # error
    #     raise Exception("i am a Exception")                 # Exception
    # except Exception as e:
    #     app('log').info(e)

    # 同步request
    # rep = app('request').get('https://api.longhash.com/', params={}, header={})
    # rep = app('request').post('https://api.longhash.com', params={}, header={})
    # print(rep.text)
    # print(rep.json())
    #
    # # 异步request
    # async def test(url, param={}):
    #     res = await app('request').aiopost(url, param)
    #     print(res.text)
    #     print(res.json())
    # app('async').run([test('https://api.longhash.com/')])              # 异步方法调用

    # config
    # print(app('config')('Config.setting.test_str', 'default'))                 # hahah123
    # print(app('config')('Config.setting.test_none', 'default'))                # default
    # print(app('config').get('Config.setting.test_tuple', 'default'))           # ('http_code', 200)
    # print(app('config').get('Config.setting.test_dict', 'default'))            # {'name': 'hahah'}
    # print(app('config').get('Config.setting.test_list', 'default'))            # [1, 2, 3, 4]
    #
    # print(app('config').get('Config.setting.test_str', 'default'))             # hahah123
    # print(app('config').get('Config.setting.test_none', 'default'))            # default

    # redis
    # res = app('redis')
    # print(res.set('name', 123))
    # print(res.get('name'))
    # print(res.select(1).get('name'))
    # print(app('redis').get('name'))

    # app容器
    # 注册类
    # class DemoA:
    #     def hello(self):
    #         return 'DemoA say hello'
    # app.register('demo', DemoA)
    # res = app('demo').hello()                 # DemoA say hello

    # 类路径注册
    # app.register('demo', '__main__.DemoA')
    # res = app('demo').hello()                   # DemoA say hello

    # 类实例注册
    # app.register('demo', DemoA())
    # res = app('demo').hello()                   # DemoA say hello

    # function 注册
    # def add(a, b):
    #     return a + b
    # app.register('add', add)                    # 方法注册
    # res = app('add')(4, 5)                      # 9

    # 数据结构注册
    # listdata = [1, 3, 22, 21, 39]
    # dictdata = {'name': 'jemes'}
    # tupledata = ('name', 'jemes')
    # base_path = str(os.path.dirname(__file__))

    # app.register('listdata', listdata)
    # app.register('dictdata', dictdata)
    # app.register('tupledata', tupledata)
    # app.register('base_path', base_path)
    # res = app('listdata')                         # [1, 3, 22, 21, 39]
    # res = app('dictdata')                         # {'name': 'jemes'}
    # res = app('tupledata')                        # ('name', 'jemes')
    # res = app('base_path')                        # /Users/jemes/workspace/simutil

    # 异步方法
    # import asyncio
    # async def hello(index):
    #     print("number:{}, Hello world!".format(index))
    #     await asyncio.sleep(1)
    #     print("end!")
    # app('async').run([hello(index) for index in range(5)])

    # oss
    # rep = app('request').get('https://api.longhash.com/', params={}, header={})
    # 上传读取的内容(内存中)
    # app('oss').referer(["http://api.longhash.com"]).push('test/api.json', rep.text, {'Content-Type': 'image/gif'})
    # # 设置referer
    # app('oss').referer(["http://api.longhash.com"]).push('test/api.json', rep.text, {'Content-Encoding': 'utf-8'})
    # # 取消referer
    # app('oss').referer().push('test/api.json', rep.text, {'Content-Encoding': 'utf-8'})
    # # 上传本地文件
    # app('oss').push_file('test/api.json', '/Users/jemes/workspace/simutil/Storage/Logs/20200528.log', {'Content-Encoding': 'utf-8'})
    # rule规则设置
    # app('oss').rule(allowed_origins=['*'], allowed_methods=['GET'], allowed_headers=['*'], max_age_seconds=100)\
    #     .push_file('test/api.json', '/Users/jemes/workspace/simutil/Storage/Logs/20200528.log')