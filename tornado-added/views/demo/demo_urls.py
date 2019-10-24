#!/usr/bin/python3
# -*- coding:utf-8 -*-


from __future__ import unicode_literals
from .demo_views import (
    demo_get_handle,
    demo_post_json_body_handle, demo_post_form)

urls = [
    (r'get', demo_get_handle),
    (r'postJsonBody', demo_post_json_body_handle),
    (r'postForm', demo_post_form),
]
