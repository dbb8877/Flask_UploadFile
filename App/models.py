# 这里创建表名、字段，并添加上传到数据库
from flask_sqlalchemy import SQLAlchemy

# 实例化数据库
db = SQLAlchemy()


# 创建学生信息表
# 这些字段怎么传进来呢？：是从中间函数views 实例化数据库类后，save过来的
class Student(db.Model):
    # 设置表名
    __tablename__ = 'student'
    __table_args__ = {"extend_existing": True}
    # id字段 ：开启自增长，设置为主键
    s_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # 字符串长度限制为20,且唯一索引
    studentName = db.Column(db.String(16), unique=True)
    # 字符串长度限制为18,且唯一索引
    studentNum = db.Column(db.String(18), unique=True)

    def __init__(self, studentName, studentNum):
        self.studentName = studentName
        self.studentNum = studentNum

    def stu_save(self):
        # db.drop_all()
        # 更新数据
        db.session.add(self)
        db.session.commit()


class Photo(db.Model):
    # 设置表名
    __tablename__ = 'student'
    __table_args__ = {"extend_existing": True}
    # 字符串长度限制为20,且唯一索引
    photoname = db.Column(db.String(255), unique=True)
    create_time = db.Column(db.String(255), unique=True)

    def __init__(self, photoname, create_time):
        self.photoname = photoname
        self.create_time = create_time

    def photo_save(self):
        db.session.add(self)
        db.session.commit()
