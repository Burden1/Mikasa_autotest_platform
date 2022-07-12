"""
    这里介绍flask-sqlalchemy的基本使用
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 1、实例化flask
app = Flask(__name__)

# 2、配置数据库信息
username = "root"
password = "yy1998123"
server = "127.0.0.1"
database = "test_platform"

app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"mysql+pymysql://{username}:{password}@{server}/{database}?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 3、将app与Flask-QLAlchemy进行绑定，实例化一个db对象
db = SQLAlchemy(app)


# 4、创建数据库模型
# 4.1、需继承db.Model
class User(db.Model):
    # 4.2、注意：如果不自定义表名的话，他生成的数据库表默认是类名（user），若类名UserInfo，表名user_info
    # 若自定义了表名，则以自定义的为准
    __tablename__ = "User"

    # 4.3、定义表字段，类型/关键字
    # 4.3.1、常用参数类型：Integer/String(20)/JSON/DateTime/Boolean/Text..
    # 4.3.2、常用关键字参数：
    # primary_key:是否主键；autoincrement 是否自增
    # nullable：是否允许为空，unique：是否允许重复
    # default：默认值
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    create_time = db.Column(db.DateTime)
    json = db.Column(db.JSON)

    def __repr__(self):
        return self.username


if __name__ == '__main__':
    # 1、创建表
    db.create_all()
    # 2、删除表
    db.drop_all()
