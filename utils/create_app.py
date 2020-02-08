from App.blue_views import student_blueprint
from flask import Flask
import os
from App.models import *
from utils import config


def create_app():
    # 返回一个从Flask_Htai_demo文件夹的绝对路径
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    # 拼接成一个static文件夹的绝对路径
    static_dir = os.path.join(BASE_DIR, 'static')
    # 拼接成一个static文件夹的绝对路径
    templates_dir = os.path.join(BASE_DIR, 'templates')

    app = Flask(__name__,
                static_folder=static_dir,
                template_folder=templates_dir)
    # 在应用对象上注册这个蓝图对象
    # 当这个应用启动后, 通过 /student/ 可以访问到蓝图中定义的视图函数
    # 实例化SQLAlchemy
    app.register_blueprint(blueprint=student_blueprint, url_prefix='/student')
    # 将config中的设置导入到app
    app.config.from_object(config)

    '''
    这里的设置被转移到config中，但仍要在这里调用 ↑
    '''
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/students?charset=utf8'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # # 设置session密钥
    # app.config['SECRET_KEY'] = 'secret_key'
    # # 设置连接的redis数据库 默认连接到本地6379
    # app.config['SESSION_TYPE'] = 'sqlalchemy'
    # # 设置远程
    # app.config['SESSION_SQLALCHEMY'] = db  # SQLAlchemy对象
    # # app.config['SESSION_PERMANENT'] = True  # 如果设置为True，则关闭浏览器session就失效。
    # # app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
    # #
    db.init_app(app)
    return app
