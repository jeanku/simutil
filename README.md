# SimUtil

python容器& libs


# 1. 安装
```
pip install simutil
```

# 2. 添加配置文件
你需要在你的项目根目录下创建一个.env文件，内容如下:

``` python
[environment]                           # 环境变量 环境变量的配置一定要放在[environment]下, 否则读取不到  
ENVIRONMENT = dev                       # 项目环境

#日志配置 
# LOG_DEBUG:日志调试模式  
LOG_DEBUG = true       
# LOG_LEVEL:DEBUG|         
LOG_LEVEL = DEBUG
# 日志路径: 每天产生一个新文件 
# 日志具体文件名: 一直记录到该文件中
LOG_PATH = /Users/**/

# redis配置
REDIS_HOST=127.0.0.1                     
REDIS_PORT=6379                          
REDIS_PASSWORD =                         
REDIS_DB=0                               

# rabbitmq 配置
RABBITMQ_HOST=127.0.0.1
RABBITMQ_PORT=5672
RABBITMQ_USER=test
RABBITMQ_PASSWORD=12345

# oss配置
OSS_ACCESS_DOMAIN=**                     
OSS_ACCESS_KEY=key                       
OSS_ACCESS_SECRET=secret                 
OSS_BUCKET_NAME=bucket_name              
OSS_END_POINT=endpoint

[default.mysql]                         # 数据库等其他配置
DB_TYPE=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=dev
DB_USER=root
DB_PASSWORD=password
DB_CHARSET=utf8mb4
```

# 3. 初始化

容器BASE_PATH注册

``` python
from simutil.App import app
import os

base_path = os.path.dirname(os.path.dirname(__file__))
app.register("BASE_PATH", os.path.dirname(os.path.dirname(__file__)))

# 注册完成之后, 你可以在代码任何地方引入app并使用
```

# 读取env配置
``` python
app('env')('LOG_PATH')                                      # 方法式读取
app('env')('LOG_PATH1', "hahaha")                           # 方法式读取(娶不到舍默认值）
app('env').LOG_PATH                                         # 属性读取
app('env')['LOG_PATH']                                      # 字典读取
app('env').items('default.mysql')                           # 模块读取 
app('env').items('sqlserver', 'DB_HOST')                    # 读取default.mysql中的DB_HOST      
app('env').items('sqlserver', 'DB_HOST1', "123")            # 读取default.mysql中的DB_HOST(带默认值)
```

# log日志
``` python
app('log').debug(("status", 0))                             # 记录tuple
app('log').info([1, 2, 3, 4, 5])                            # 记录list
app('log').error({'name':'jemes'})                          # 记录dict
app('log').warning("123444")                                # 记录string    
app('log').critical(5)                                      # 记录number
try:
    a = 100 / 0                                             # error
    raise Exception("i am a Exception")                     # Exception
except Exception as e:
    app('log').info(e)                                      # 记录error or exception
```

# 网络请求request
``` python
# 同步request get
rep = app('request').get('https://api.longhash.com/', params={}, header={})
text = rep.text
json = rep.json()

# 同步request post
rep = app('request').post('https://api.longhash.com', params={}, header={})
text = rep.text
json = rep.json()

# 异步request get
async def test(url, param={}):
    res = await app('request').aiogett(url, param)
    text = res.text
    json = res.json()
app('async').run([test('https://api.longhash.com/')])              # 异步方法调用

# 异步request post
async def test(url, param={}):
    res = await app('request').aiopost(url, param)
    text = res.text
    json = res.json()
app('async').run([test('https://api.longhash.com/')])              # 异步方法调用
```


# 读取项目中配置文件信息
``` python
# config 读取app 注册的BASE_PATH下文件配置
app('config')('Config.setting.test_str')                            # {BASE_PATH}/Config/setting.py test_str值
app('config')('Config.setting.test_str', 'default')                 # {BASE_PATH}/Config/setting.py test_str值 取不到则用默认值default
app('config').get('Config.setting.test_str', 'default')             # {BASE_PATH}/Config/setting.py test_str值 字典方式读取
```


# redis
``` python
# redis
app('redis').set('name', 123)                                       # 设置key                                 
app('redis').get('name')                                            # 读取key
app('redis').select(1).get('name')                                  # 切换redis DB: 1

# 如果想使用其他非 .env中的配置的redis， 建议使用app.register 注册新的redis实例
from simutil.Redis import Redis
redis = Redis(app('env').REDIS_HOST, app('env').REDIS_PORT)
app.register('redis1', redis)
app('redis1').get('testname')
```


# async方法
``` python
# 异步方法
import asyncio
async def hello(index):                                 # 自定义的async方法
    print("number:{}, Hello world!".format(index))
    await asyncio.sleep(1)
    print("end!")
app('async').run([hello(index) for index in range(5)])  # 执行

```

# 阿里OSS
``` python
# oss
rep = app('request').get('https://api.***.com/index', params={}, header={})

# 上传读取的内容(从内存中)
app('oss').push('oss/api.json', rep.text)                   # oss/api.json为上传到oss的文件路径名称             

# 设置referer
app('oss').referer(["http://api.longhash.com"]).push('test/api.json', rep.text, {'Content-Encoding': 'utf-8'})

# 取消referer 或设置为空
app('oss').referer().push('test/api.json', rep.text, {'Content-Encoding': 'utf-8'})

# 上传本地文件
filepath = /Users/jemes/workspace/simutil/Storage/Logs/20200528.log
app('oss').push_file('test/api.json', filepath, {'Content-Encoding': 'utf-8'})

# rule规则设置
app('oss').rule(allowed_origins=['*'], allowed_methods=['GET'], allowed_headers=['*'], max_age_seconds=100)\
    .push_file('test/api.json', '/Users/jemes/workspace/simutil/Storage/Logs/20200528.log')
```

# Path路径
``` python
rep = app('path')                               # 指向BASE_PATH的Pathlib对象
base_path = app('path').resolve()               # = app('BASE_PATH')
config_path = rep.joinpath('Config')            # {BASE_PATH}/Config
logs_path = rep.joinpath('Storage/Logs')        # {BASE_PATH}/Storage/Logs
# 其他操作和Pathlib一致                                             
```

# rabbitMQ
``` python
rab = app('rabbitmq')                           # 指向BASE_PATH的Pathlib对象
conn = rab.connection()                         # rabbitmq connection
channel = rab.channel()                         # rabbitmq channel                                           
```

# App容器
``` python
# 为了实现代码结偶和复用, 延时加载
# 说明: app('keyname') 拿出来的都是单例, App本身也是单例模式

# 注册class
class DemoA:
    def hello(self):
        return 'DemoA say hello'
demo1 = app.register('demo1', DemoA)                     # 类名注册
demo2 = app.register('demo2', '__main__.DemoA')          # 类路径注册(我在main函数中执行的，所以路径为__main__.DemoA)
demo3 = app.register('demo', DemoA())                    # 实例注册
res = app('demo1').hello()                               # print: DemoA say hello
res = app('demo2').hello()                               # print: DemoA say hello
res = app('demo3').hello()                               # print: DemoA say hello


# 注册function
def add(a, b):
    return a + b
app.register('add', add)                                 # 方法注册
res = app('add')(4, 5)                                   # print: 9

# 注册数据
app.register('listdata', [1, 3, 22, 21, 39])                      
app.register('dictdata', {'name': 'jemes'})
app.register('tupledata', ('name', 'jemes'))
app.register('base_path', str(os.path.dirname(__file__)))
res = app('listdata')                                    # print: [1, 3, 22, 21, 39]
res = app('dictdata')                                    # print: {'name': 'jemes'}
res = app('tupledata')                                   # print: ('name', 'jemes')
res = app('base_path')                                   # print: /Users/jemes/workspace/simutil
```