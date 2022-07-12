"""
    这里简单介绍flask的基本使用
    前提： pip install flask
"""
from flask import Flask

# 1、创建app实例
app = Flask(__name__)


# 2、定义路由及视图函数
@app.route("/demo")
def hello_world():
    return "HelloWorld"


# 2、定义动态路由及视图函数
@app.route("/getname/<username>")
def getname(username):
    return username


# 3、定义【限定类型】路由及视图函数
# 类型包括5种：string，int，float，path，uuid
@app.route("/post/<string:username>")
def get(username):
    return username


# 4、路由的尾部带有"/"(浏览器的地址栏中输入和不输入“/”的效果一样)
# 路由的尾部没有“/”（输入的URL的结尾不能加 “/”，会报错404）
# 类型包括5种：string，int，float，path，uuid
@app.route("/demo2/")
def print():
    return "地址栏尾部有/"


# 定义http请求：get/post/put/delete
# 5、定义【get/post/put/delete请求】路由及视图函数
# 注意：methods,里面是一个列表
@app.route("/testcase", methods=["get"])
# @app.route("/testcase", methods=["post"])
# @app.route("/testcase", methods=["put"])
# @app.route("/testcase", methods=["delete"])
def get_case():
    return {"code": 0, "msg": "get success"}


if __name__ == '__main__':
    # debug为true，是热加载，更改完进行保存就能查看到效果
    # 指定host为局域网
    app.run(debug=True, host="0.0.0.0")
