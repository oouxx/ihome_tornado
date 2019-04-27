# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import os
from libs.tornadosql import tornadosql
import config
import redis

from handlers import Passport
from urls import urls
from tornado.options import options, define
from tornado.web import RequestHandler

"""
tornado.options模块
tornado.options.define()
    用来定义options选项变量的方法，定义的变量可以在全局的tornado.options.options中获取使用.
tornado.options.options
    全局的options对象，所有定义的选项变量都会作为该对象的属性。
tornado.options.parse_command_line()
    转换命令行参数，并将转换后的值对应的设置到全局options对象相关属性上。追加命令行参数的方式是--myoption=myvalue
tornado.options.parse_config_file(path)
    从配置文件导入option，配置文件中的选项格式如下：
    myoption = "myvalue"
    myotheroption = "myothervalue"
"""
define("port", default=8000, type=int, help="run server on the given port")

"""
数据库连接放在Application中
注意Application与RequestHandler的关系:
    在RequestHandler对象中存在当前application对象(创建application对象的时候传入了RequestHandler)
"""


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.db = tornadosql.Connection(**config.mysql_options)
        self.redis = redis.StrictRedis(**config.redis_options)


def main():

    """
    配置日志属性,如果没有调用parse_command_line()的配置不会设置到options中
    """
    options.log_file_prefix = config.log_path
    options.logging = config.log_level
    tornado.options.parse_command_line()

    """
    Application对象
        urls是list,list内的元素是tuple,tuple内的元素是一个字符串和一个RequestHandler或起子类对象.
        settings是一个字典
    """
    app = Application(
        urls,
        **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    """单进程"""
    http_server.listen(options.port)
    """
    # 多进程,bind(port) 端口号,start(num_process) 进程数,0表示自动获取cpu核心数
    http_server.bind(8000)
    http_server.start(0)
    """
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
