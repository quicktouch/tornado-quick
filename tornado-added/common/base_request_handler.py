#! /usr/bin/python3
# -*- coding:utf-8 -*-
import traceback
from typing import Optional, Awaitable
import tornado.web

from common.commons import http_error_response, http_error_with_reason
from conf.base import DEBUG


class base_request_handler(tornado.web.RequestHandler):

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    # 设置统一的http响应头 https://stackoverflow.com/questions/42434645/set-headers-for-all-requests-in-tornado
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json;charset=UTF-8")

    # 设置统一的错误返回
    def write_error(self, status_code, **kwargs):
        error_trace_list = traceback.format_exception(*kwargs.get("exc_info"))
        if DEBUG:
            reason = ""
            if len(error_trace_list) > 0:
                reason = error_trace_list[-1]
            http_error_with_reason(self, status_code, reason)
        else:
            http_error_response(self, status_code)
