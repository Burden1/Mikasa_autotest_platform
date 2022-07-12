"""
    这里介绍Flask Restx 接口配置的基本使用2
    前提：pip install flask-restx
    使用restful风格规范接口
"""
from flask import Flask

from flask_restx import Api, Resource

# 1、创建app实例
app = Flask(__name__)
# 2、创建api实例
api = Api(app)


# 接口路径定义在类上，对应不同请求操作创建不同的方法
@api.route("/user")
# 注意：类要继承Resource
class User(Resource):
    # 1、restful风格get方法
    def get(self):
        return {'code': 0, "msg": "get success"}

    # 2、restful风格post方法
    def post(self):
        return {'code': 0, "msg": "post success"}

    # 3、restful风格put方法
    def put(self):
        return {'code': 0, "msg": "put success"}

    # 4、restful风格delete方法
    def delete(self):
        return {'code': 0, "msg": "delete success"}


if __name__ == '__main__':
    app.run(debug=True)
