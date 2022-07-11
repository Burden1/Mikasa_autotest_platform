"""
    测试用例控制层，即路由层
    接收前端请求，返回后端结果
"""

from flask import request
from flask_restx import Namespace, Resource

from do.testcase_entity import TestCaseEntity
from app import api
from service.testcase_service import TestcaseService
from utils.log_utils import logger

# 命名空间
case_ns = Namespace("case", description="用例管理")
testcase_service = TestcaseService()


@case_ns.route("")
class TestCaseController(Resource):
    get_paresr = api.parser()
    get_paresr.add_argument("id", type=int, location="args")

    @case_ns.expect(get_paresr)
    def get(self):
        """
        查询测试用例（单个/所有）
        :return:
        """
        # 拿到请求参数用例id
        case_id = request.args.get("id")
        logger.info(f"接收到的参数 <===== {case_id}")
        if case_id:
            # 若传参用例id，则根据id查
            # as_dict()作用： 把python对象转换成前端可以使用的json
            testcase_datas = [testcase_service.get(case_id).as_dict()]
        else:
            # 否则查询所有
            datas = testcase_service.get_list()
            # 注意，返回的要是一个字典结构，否则前端接收不了
            testcase_datas = [data.as_dict() for data in datas]
        return {"code": 0, "msg": {"data": testcase_datas}}

    post_paresr = api.parser()
    post_paresr.add_argument("id", type=int, required=True, location="json")
    post_paresr.add_argument("case_title", type=str, required=True, location="json")
    post_paresr.add_argument("remark", type=str, location="json")

    @case_ns.expect(post_paresr)
    def post(self):
        """
        新增测试用例
        :return:
        """
        # 获取请求数据
        case_data = request.json
        testcase_entity = TestCaseEntity(**case_data)
        res = testcase_service.save(testcase_entity)
        if res:
            return {"code": 0, "msg": f"case id {res} success add."}
        else:
            return {"code": 40001, "msg": "case is exists"}

    put_paresr = api.parser()
    put_paresr.add_argument("id", type=int, required=True, location="json")
    put_paresr.add_argument("case_title", type=str, required=True, location="json")
    put_paresr.add_argument("remark", type=str, location="json")

    @case_ns.expect(put_paresr)
    def put(self):
        """
        测试用例的修改
        :return:
        """
        case_data = request.json
        testcase_entity = TestCaseEntity(**case_data)
        res = testcase_service.update(testcase_entity)
        if res:
            return {"code": 0, "msg": f"case id {res} success change "}
        else:
            return {"code": 40002, "msg": "case is not exists"}

    delete_parser = api.parser()
    delete_parser.add_argument("id", type=int, location="json", required=True)

    @case_ns.expect(delete_parser)
    def delete(self):
        """
        根据用例id删除测试用例
        :return:
        """
        case_data = request.json
        case_id = case_data.get("id")
        logger.info(f"接收到的参数id <====={case_id}")
        res = testcase_service.delete(case_id)
        if res:

            return {"code": 0, "msg": f"case id {case_id} success delete"}
        else:
            return {"code": 40002, "msg": f"case is not exists"}
