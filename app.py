"""
    启动类
"""
import yaml
from flask import Flask
from flask_restx import Api, Namespace
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

# 用例的命名空间，CORS解决跨域问题
CORS(app, supports_credentials=True)

# 数据库配置
# 读取数据库配置
with open("../config/data.yml", encoding='utf-8') as f:
    result = yaml.safe_load(f)
    username = result.get("database").get('username')
    password = result.get("database").get('password')
    server = result.get("database").get('server')
    database = result.get("database").get('database')

app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"mysql+pymysql://{username}:{password}@{server}/{database}?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# SQLALchemy 绑定app
db = SQLAlchemy(app)
db_session: Session = db.session


def add_router():
    from controller.testcase_controller import case_ns
    from controller.plan_controller import plan_ns
    from controller.build_controller import build_ns
    # 添加api的命名空间，解决swagger不展示内容的问题
    api.add_namespace(case_ns, "/testcase")
    api.add_namespace(plan_ns, "/plan")
    api.add_namespace(build_ns, "/build")


if __name__ == '__main__':
    add_router()
    app.run(debug=True, host="0.0.0.0", port=8888)
