#! /usr/bin/python3
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from .users_views import (
    RegistHandle,
    LoginHandle
)

urls = [
    # 从 /users/regist 过来的请求，将调用 users_views 里面的 RegistHandle 类
    (r'regist', RegistHandle),
    (r'ping', RegistHandle),
    (r'login', LoginHandle)
]
