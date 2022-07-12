"""
    这里介绍flask_restx，集成swagger的基本使用
    swagger可以理解为API接口文档，便于前后端分离项目中的使用
    前端可以直接访问文档进行接口调用，类似于postman
"""

from flask import Flask
from flask_restx import Api, Namespace, Resource

app = Flask(__name__)
api = Api(app)

# 1、定义命名空间
case_ns = Namespace("case", description="用例管理")


# 2、为类添加装饰器@namespace.route("")控制子路由
@case_ns.route("")
class TestCase(Resource):
    # 3、定义parser解析器对象
    get_paresr = api.parser()
    # 4、通过parser对象添加参数
    # 第一个参数是参数名，后面是关键字传参：
    # 4.1、type：类型（int/bool/float/string/FileStorage）；
    # 4.2、required约束控制（True/False）
    # 4.3、choices枚举参数
    # 4.4、location对应request对象中的属性（args/form/json/files）
    # 注意：一般get请求location都是args，
    # post请求可以为/form/json/files，但是呢file和json不能共存，form和json也不能共存
    # 也就是调用add_argumet()时，添加参数不能同时有location=file/json
    get_paresr.add_argument("id", type=int, location="args")

    # 5、添加装饰器
    @case_ns.expect(get_paresr)
    def get(self):
        return {'code': 0, 'msg': "get success"}


# 6、为命名空间指定访问资源路径,可以理解为访问的是/case底下的get/post..方法，命名空间为：用例管理
api.add_namespace(case_ns, '/case')

if __name__ == '__main__':
    app.run(debug=True)
