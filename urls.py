# coding:utf-8

import os

from handlers.BaseHandler import StaticFileBaseHandler as StaticFileHandler
from handlers import Passport, VerifyCode, Profile, House, Orders

'''
    url作为传给Application的一个参数：
    Application(self,handlers=None,default_host=None,transforms=None,**setings)
    
    tornado.web.StaticFileHandler是框架自带用于处理静态文件的路由映射，这里为了实现xsrf_token，
    创建了一个继承自StaticFielHandler的子类
    在Application中配置StaticFileHandler处理路由的是有需要配置一个路径字典
    application = web.Application([
        (r"/content/(.*)", web.StaticFileHandler, {"path": "/var/www"}),
    另外一个参数是default_filename=''为制定默认的文件名
    一般在给路径的时候采用相对路径，通过os.path.dirname获取当前文件夹的名字，join拼接字符串成路径

    tornado.web.RequestHandler 是tornado用来处理HTTP请求的类
    该类通常传递三个参数:RequestHandler(self,application,request,**kwargs)
    对于Application，第一个参数handlers是一个列表，这个列表由多个路由元组组成，
    每个元组有多个个参数，一个uri,一个基于RequestHandler或和web的其他handler的子类，
        还有一个可选的字典，将传入到RequestHandler的initialized()中
    如果有需要给路由取名，则需要通过tornado.web.url来构建该元组
        如url(r'(/)',MyHandler,{},name='python_url')
        取名可以通过调用RequestHandler.reverse_url(name)还获取该名字对应的url

# 注意url的匹配是短路匹配原则，如果r'/(.*)'放在地一个，所有的请求都会只走这个路由
'''
urls = [
    # (r"/log", Passport.LogHandler),
    (r"/api/register", Passport.RegisterHandler),
    (r"/api/login", Passport.LoginHandler),
    (r"/api/logout", Passport.LogoutHandler),
    (r"/api/check_login", Passport.CheckLoginHandler),  # 判断用户是否登录
    (r"/api/piccode", VerifyCode.PicCodeHandler),       # 图片验证码
    # (r"/api/smscode", VerifyCode.SMSCodeHandler),
    (r"/api/profile/avatar", Profile.AvatarHandler),  # 用户上传头像
    (r"/api/profile", Profile.ProfileHandler),  # 个人主页获取个人信息
    (r"/api/profile/name", Profile.NameHandler),  # 个人主页修改用户名
    (r"/api/profile/auth", Profile.AuthHandler),  # 实名认证
    (r"/api/house/area", House.AreaInfoHandler),  # 城区信息
    (r'^/api/house/info$', House.HouseInfoHandler),  # 上传房屋的基本信息
    (r'^/api/house/image$', House.HouseImageHandler),  # 上传房屋图片
    (r'^/api/house/my$', House.MyHousesHandler),  # 查询用户发布的房源
    (r'^/api/house/index$', House.IndexHandler),  # 首页
    (r'^/api/house/list$', House.HouseListHandler),  # 房屋过滤列表数据
    (r'^/api/house/list2$', House.HouseListRedisHandler),  # 房屋过滤列表数据
    (r'^/api/order$', Orders.OrderHandler),  # 下单
    (r'^/api/order/my$', Orders.MyOrdersHandler),  # 我的订单，作为房客和房东同时适用
    (r'^/api/order/accept$', Orders.AcceptOrderHandler),  # 接单
    (r'^/api/order/reject$', Orders.RejectOrderHandler),  # 拒单
    (r'^/api/order/comment$', Orders.OrderCommentHandler),
    (r"/(.*)", StaticFileHandler,
     dict(path=os.path.join(os.path.dirname(__file__), "html"), default_filename="index.html"))
]
