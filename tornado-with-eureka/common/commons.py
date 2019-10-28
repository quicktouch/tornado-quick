#! /usr/bin/python3
# -*- coding:utf-8 -*-

import json
import os

from conf.base import ERROR_CODE


def http_success_response(self, data, msg="ok"):
    """
    请求成功时的返回的数据格式
    :param self:  response
    :param data:  成功返回的数据
    :param msg:   错误提示信息
    """
    self.write(json.dumps({
        "succ": True,
        "code": 1,
        "msg": msg,
        "data": data
    }))


def http_error_response(self, code=-1, msg="failed"):
    """
    返回失败的数据格式
    :param self:  response
    :param code:  错误编码,默认为-1
    :param msg:   错误提示信息,如果不提供信息,则使用错误编码对应的错误提示或使用默认错误信息
    """
    show_msg = msg
    if msg is None or msg == "failed":
        try:
            show_msg = ERROR_CODE[code]
        except:
            show_msg = "failed"
    self.write(json.dumps({
        "succ": False,
        "code": code,
        "msg": show_msg
    }))


def http_error_with_reason(self, code=-1, reason="", msg="failed"):
    """
    返回失败的数据格式
    :param reason: 错误原因
    :param self:  response
    :param code:  错误编码,默认为-1
    :param msg:   错误提示信息,如果不提供信息,则使用错误编码对应的错误提示或使用默认错误信息
    """
    show_msg = msg
    if msg is None or msg == "failed":
        try:
            show_msg = ERROR_CODE[code]
        except:
            show_msg = "failed"
    self.write(json.dumps({
        "succ": False,
        "code": code,
        "msg": show_msg,
        "reason": reason
    }))


def save_files(file_metas, in_rel_path, type='image'):
    """
    保存图片
    """
    file_path = ""
    file_name_list = []
    for meta in file_metas:
        file_name = meta['filename']
        file_path = os.path.join(in_rel_path, file_name)
        file_name_list.append(file_name)
        # save image as binary
        with open(file_path, 'wb') as up:
            up.write(meta['body'])
    return file_name_list


if __name__ == "__main__":
    http_success_response()

"""
返回格式举例
    
    成功
    {
        "msg": "ok",
        "code": 1,
        "succ": true,
        "data": {
            "total": 3,
            "size": 10,
            "current": 1,
            "records": [                          
            ],
            "pages": 1
        },
        "oper": "land monitor search list"
    }
    
    失败
    {
        "msg": "参数缺失",
        "code": -1,
        "succ": false
    }
"""
