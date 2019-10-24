# 主程序入口
# ! /usr/bin/python3
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import os
from tornado.options import define
# 引入主路由函数
from views.url_router import include, url_wrapper


class Application(tornado.web.Application):
    def __init__(self):
        handlers = url_wrapper([
            (r"/users/", include('views.users.users_urls')),
            (r"/upload/", include('views.upload.upload_urls')),
            (r"/demo/", include('views.demo.demo_urls'))
        ])
        # 定义 Tornado 服务器的配置项，如 static/templates 目录位置、debug 级别等
        settings = dict(
            debug=True,
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates")
        )
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    print("Tornado server is ready for service\r")
    tornado.options.parse_command_line()
    Application().listen(8000, xheaders=True)
    tornado.ioloop.IOLoop.instance().start()
