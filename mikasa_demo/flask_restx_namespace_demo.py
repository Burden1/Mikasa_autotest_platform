"""
    这里介绍Flask-Restx namespace的使用
"""
from flask import Flask
from flask_restx import Api, Namespace, Resource

app = Flask(__name__)
api = Api(app)

# 1、定义Namespacce实例
hello_ns = Namespace("demo", description="demo管理")
case_ns = Namespace("case", description="用例管理")


# 2、为类添加装饰器@namespace.route("")控制子路由
@case_ns.route("")
class TestCase(Resource):
    def get(self):
        return {'code': 0, 'msg': "get success"}

    def post(self):
        return {'code': 0, 'msg': "post success"}


# 3、为命名空间指定访问资源路径,可以理解为访问的是/case底下的get/post..方法，命名空间为：用例管理
api.add_namespace(case_ns, '/case')

if __name__ == '__main__':
    app.run(debug=True)
