"""
    这里介绍Flask Restx 接口配置的基本使用
    前提：pip install flask-restx
    他是一个支持Restful的flask插件，用于规范化接口的编写，并且支持swagger文档
"""
from flask import Flask
from flask_restx import Api, Resource


# 1、创建app实例
app = Flask(__name__)
# 2、创建Api实例
api = Api(app)


# 3、定义路由及视图函数
#  注意：装饰器改为使用@api.route("")
#  类里面要继承Resource类
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


# 4、启动
if __name__ == '__main__':
    app.run(debug=True)
