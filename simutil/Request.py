#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


class Request():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Request, cls).__new__(cls, *args, **kwargs)
            return cls._instance

    def get(self, url, params=None, header=None, timeout=5, **kwargs):
        return requests.get(url, params=params, headers=header, timeout=timeout, **kwargs)

    def post(self, url, params={}, timeout=5, header=None, **kwargs):
        return requests.post(url, data=params, headers=header, timeout=timeout, **kwargs)

    # 请求网络数据
    async def aiorequest(self, method, url, headers={}, params={}, data={},  **kwargs):
        import aiohttp
        async with aiohttp.ClientSession() as session:
            async with session.__getattribute__(method)(url, params=params, data=data, headers=headers, **kwargs) as response:
                res = await response.text()
                return Response(res)

    async def aioget(self, url, params={}, headers={}, **kwargs):
        return await self.aiorequest('get', url, params=params, headers=headers, **kwargs)

    async def aiopost(self, url, params={}, headers={}, **kwargs):
        return await self.aiorequest('post', url, data=params, headers=headers, **kwargs)


class Response():
    def __init__(self, text):
        self._text = text

    @property
    def text(self):
        return self._text

    def json(self):
        import json
        return json.loads(self._text)
