#! /usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional, Awaitable
import tornado.web


class base_request_handler(tornado.web.RequestHandler):

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    # 设置统一的http响应头 https://stackoverflow.com/questions/42434645/set-headers-for-all-requests-in-tornado
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json;charset=UTF-8")
