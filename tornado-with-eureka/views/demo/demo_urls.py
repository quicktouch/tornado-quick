#!/usr/bin/python3
# -*- coding:utf-8 -*-


from __future__ import unicode_literals
from .demo_views import (
    DemoGetHandle,
    DemoPostJsonBodyHandle, DemoPostForm)

urls = [
    (r'get', DemoGetHandle),
    (r'postJsonBody', DemoPostJsonBodyHandle),
    (r'postForm', DemoPostForm),
]
