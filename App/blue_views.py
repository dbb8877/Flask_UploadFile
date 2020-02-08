from App.models import Student, Photo
from flask import Flask, Blueprint, request, render_template, redirect, url_for, session, flash
import os, json
from datetime import datetime

app = Flask(__name__)

# 创建蓝图
student_blueprint = Blueprint('student', __name__)


@student_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    """
    用户输入信息页面
    """
    # 实例化按钮
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':

        '''
        加一个返回首页的按钮
        '''
        if 'up' in request.form:
            return redirect(url_for('student.home'))
        # 获取学生信息
        studentName = request.form.get('studentName')
        studentNum = request.form.get('studentNum')
        session['studentName'] = studentName
        session['studentNum'] = studentNum
        # 定义个变量来控制过滤用户填写的信息
        # 判断用户是否信息都填写了.(all()函数可以判断用户填写的字段是否有空)
        if not all([studentName, studentNum]):
            msg = '* 请填写完整信息'
            return render_template('register.html', msg=msg)
        # 判断身份证号长度是否等于18位
        if len(studentNum) != 18:
            msg = '* 请输入18位身份证号码'
            return render_template('register.html', msg=msg)
        '''
        查询数据库中身份证号是否已经存在
            1.如果存在，则返回一个确认更改弹窗：
                (在js里完成定向)
                您的信息已经存在，点击'yes'：定向到上传图片；
                点击'no'：定向到当前网页

        '''
        student_base = Student.query.filter_by(studentNum=studentNum).first()
        if student_base:
            base = student_base
            return render_template('register.html', base=base, studentNum=studentNum, studentName=studentName)
        '''
            2.如果不存在，添加数据。
        '''
        # 将学生信息保存在session中

        # 核对输入的用户是否已经被注册了
        # stu = Student.query.filter(Student.studentNum == studentNum).first()
        # 上面的验证全部通过后就开始创建新用户
        # 实例化Student类
        student = Student(studentName=studentName, studentNum=studentNum)
        # 调用save函数存注册的用户
        student.stu_save()
        # 跳转到传照片页面
        name = studentName
        return redirect(url_for('student.upload_pic', name=name))


# set()内部传递的是无序的独特的组合，必须传递两个以上，并用[]集合
ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg'])


def allow_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@student_blueprint.route('/upload_pic/', methods=['GET', 'POST'])
def upload_pic():
    if request.method == 'GET':
        return redirect(url_for('student.register'))
    if request.method == 'POST':
        '''
        在数据据上储存图片的路径和储存的时间
        '''
        # photo 是前端 name='photo'
        file = request.files['photo']
        # 获取上传图片的大小
        pic_size = len(file.read())
        # 通过session获取身份证号码，然后拼接后缀
        studentname = session.get('studentName')
        studentnum = session.get('studentNum')
        # 如果满足上传条件后的操作
        # filename是‘获取上传的文件名’的方法
        if file and allow_file(file.filename) and pic_size <= 2 * 1024 * 1024:  # 存在file and 支持后缀 (is True可省略)
            # 获取上传文件的后缀名
            suffix = os.path.splitext(file.filename)[1]
            # 生成学生身份证的文件名，然后拼接后缀
            photo_name = studentnum + suffix
            '''
            将上传的图片储存在本地（指定位置）
            '''
            # # 文件写入磁盘，参数是文件的绝对路径或者相对路径
            # file.save(photoname)
            # 相对路径+文件名
            photo_name = os.path.join('./photo/', photo_name)
            file.save(photo_name)
            create_time = datetime.now()
            '''
            在原有集合基础上添加数据(修改数据):
                建立一个修改数据的依据
            '''
            photo_base = Photo.query.filter_by(studentName=studentname, studentNum=studentnum).first()
            # '''
            # 查看是否已经上传过照片
            #     (在js里完成)
            #     1.如果已经上传照片，弹框返回。
            # '''
            # if not photo_base:
            #     return render_template('upload_pic.html', studentname=studentname,
            #                            photoname=photo_name,
            #                            create_time=create_time)

            photo_base.photoname = photo_name
            photo_base.create_time = create_time
            photo_base.photo_save()
            photo_var = Photo.query.filter_by(photoname=photo_name).first()
            if photo_var:
                flash('图片上传成功！')
                return render_template('upload_pic.html', studentname=studentname)
        # 如果不满足上传条件时的提示
        else:
            if not allow_file(file.filename):
                # 复习一下flash
                flash("请上传'jpg', 'png', 'jpeg'类型文件")
                return render_template('upload_pic.html')
            if pic_size > 2 * 1024 * 1024:
                msg, flag = "上传失败，照片必须小于2M", False
                return render_template('upload_pic.html', msg=msg)
        # url_for的参数中 student代表创建蓝图的名称 home代码注册蓝图的函数
        return redirect(url_for('student.home'))


# 设置一个返回首页的蓝图函数
@student_blueprint.route('/home/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        return render_template('home.html')
