#! /usr/bin/python3
# -*- coding:utf-8 -*-
import py_eureka_client.eureka_client as eureka_client

# 服务器端 IP+Port，请修改对应的IP  访问静态文件的话可能会用到
SERVER_HEADER = "http://localhost:8000"

DEBUG = True

ERROR_CODE = {
    0: "ok",
    -1: "failed",
    404: "地址不存在",
    1001: "入参非法",
}

EUREKA_SERVER_LIST = "http://127.0.0.1:8761/eureka"
SERVER_HOST = "10.10.38.20"
SERVER_PORT = 8000

def register_eureka():
    # 配置Euraka 文档见: https://github.com/keijack/python-eureka-client/blob/master/README.zh_cn.md
    # 仅提供对外的服务即可
    # The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
    eureka_client.init_registry_client(eureka_server=EUREKA_SERVER_LIST,
                                       app_name="economic-model",
                                       instance_host=SERVER_HOST,
                                       instance_port=SERVER_PORT)
