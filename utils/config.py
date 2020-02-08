from App.models import *

HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'students'
USERNAME = 'root'
PASSWORD = 'root'

DB_URI = "mysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME, password=PASSWORD,
                                                                                host=HOST, port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
# # 一个将会绑定多种数据库的字典
# SQLALCHEMY_BINDS = {
#     'users':        'mysqldb://localhost/users',
#     'appmeta':      'sqlite:////path/to/appmeta.db'
# }
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 调试设置为true
SQLALCHEMY_ECHO = True
SECRET_KEY = 'secret_key'
SESSION_TYPE = 'sqlalchemy'
SESSION_SQLALCHEMY = db
# 自动回收连接的秒数。这对 MySQL 是必须的，
# 默认 情况下 MySQL 会自动移除闲置 8 小时或者以上的连接。
# 需要注意地是如果使用 MySQL 的话， Flask-SQLAlchemy 会自动地设置这个值为 2 小时。
# SQLALCHEMY_POOL_RECYCLE = 1200  # 秒
# 如果设置为True，则关闭浏览器session就失效
SESSION_PERMANENT = True
# 是否对发送到浏览器上session的cookie值进行加密
# SESSION_USE_SIGNER = False
