from .Env import Env
import oss2
from oss2.models import BucketCors, CorsRule, BucketReferer


class Oss():
    '''
    阿里OSS服务类
    '''
    _oss_sinstance = None

    def __init__(self, access_key=None, access_secret=None, end_point=None, bucket_name=None):
        if access_key is not None:
            self._oss_sinstance = oss2.Bucket(
                oss2.Auth(access_key, access_secret), end_point, bucket_name
            )
        else:
            env = Env()
            self._oss_sinstance = oss2.Bucket(
                oss2.Auth(env('OSS_ACCESS_KEY'), env('OSS_ACCESS_SECRET')),
                env('OSS_END_POINT'), env('OSS_BUCKET_NAME'),
            )

    def push(self, filename, content, header=None):
        '''
        上传文件
        :param filename: 上传文件名， 例如：'data/test.json'
        :param content: 上传的文件内容
        :param header: header
        :return:
        '''
        return self._oss_sinstance.put_object(filename, content, headers=header)

    def push_file(self, filename, local_filename, header=None):
        '''
        上传本地文件
        :param filename: 上传文件名， 例如：'data/test.json'
        :param local_filename: '本地文件路径'
        :param header: header
        :return:
        '''
        return self._oss_sinstance.put_object_from_file(filename, local_filename, headers=header)

    def rule(self, allowed_origins=['*'], allowed_methods=['GET', 'POST', 'HEAD'], allowed_headers=['*'],
             max_age_seconds=600):
        '''
        处理跨域
        :param allowed_origins: 来源
        :param allowed_methods: 接受的请求方法
        :param allowed_headers: 接受的请求头
        :param max_age_seconds: 缓存时间（秒）
        :return:
        '''
        rule = CorsRule(allowed_origins=allowed_origins, allowed_methods=allowed_methods,
                        allowed_headers=allowed_headers, max_age_seconds=max_age_seconds)
        self._oss_sinstance.put_bucket_cors(BucketCors([rule]))
        return self

    def referer(self, referers=None):
        '''
        防盗链
        :param referers: ['http://www.longhash.com', 'http://api.longhash.com']
        :return: self
        '''
        if referers is not None:
            self._oss_sinstance.put_bucket_referer(BucketReferer(False, referers))
        else:
            self._oss_sinstance.put_bucket_referer(BucketReferer(True, []))
        return self
