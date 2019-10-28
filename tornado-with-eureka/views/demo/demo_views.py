#! /usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional, Awaitable

from tornado.escape import json_decode
import logging
from logging.handlers import TimedRotatingFileHandler

# 从commons中导入http_response方法
from common.commons import (
    http_success_response,
    http_error_response,
)

########## Configure logging #############
from common.base_request_handler import BaseRequestHandler

logFilePath = "log/users/users.log"
logger = logging.getLogger("Users")
logger.setLevel(logging.DEBUG)
handler = TimedRotatingFileHandler(logFilePath,
                                   when="D",
                                   interval=1,
                                   backupCount=30)
formatter = logging.Formatter('%(asctime)s \
%(filename)s[line:%(lineno)d] %(levelname)s %(message)s', )
handler.suffix = "%Y%m%d"
handler.setFormatter(formatter)
logger.addHandler(handler)


class DemoGetHandle(BaseRequestHandler):
    """
    接受get方法 获取url后的参数，或者获取x-www-url-encoded格式的参数
    """

    def get(self):
        try:
            phone = self.get_argument("phone")
            password = self.get_argument("password")
        except KeyError:
            # 获取入参失败时，抛出错误码及错误信息
            logger.info("RegistHandle: request argument incorrect")
            http_error_response(self, 1001)
            return
        logger.debug("RegistHandle: regist successfully")
        http_success_response(self, {"phone": phone, "password": password}, "注册成功")


class DemoPostJsonBodyHandle(BaseRequestHandler):
    """
    post请求,接受http请求体
    """

    def post(self):
        try:
            # 获取入参
            args = json_decode(self.request.body)
            phone = args['phone']
            password = args['password']
        except KeyError:
            # 获取入参失败时，抛出错误码及错误信息
            logger.info("RegistHandle: request argument incorrect")
            http_error_response(self, 1001)
            return
        logger.debug("RegistHandle: regist successfully")
        http_success_response(self, {"phone": phone, "password": password}, "postJsonBody发送成功")

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass


class DemoPostForm(BaseRequestHandler):
    """
        post请求,接受x-www-url-encoded格式的参数
    """

    def post(self):
        try:
            phone = self.get_argument("phone")
            password = self.get_argument("password")
        except KeyError:
            # 获取入参失败时，抛出错误码及错误信息
            logger.info("demo_post_form: request argument incorrect")
            http_error_response(self, 1001)
            return
        logger.debug("demo_post_form:success")
        http_success_response(self, {"phone": phone, "password": password}, "demo_post_form成功")

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass
