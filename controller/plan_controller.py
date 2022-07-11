"""
    测试计划控制层
    引用Swagger
"""
import json

from flask import request
from flask_restx import Namespace, Resource

from do.plan_enetity import PlanEntity
from app import api
from service.plan_serivce import PlanService
from utils.log_utils import logger

plan_service = PlanService()
plan_ns = Namespace("plan", description="测试计划管理")


@plan_ns.route("")
class PlanController(Resource):
    get_paresr = api.parser()
    get_paresr.add_argument("id", type=int, location="args")

    @plan_ns.expect(get_paresr)
    def get(self):
        """
        查询测试计划（查询单个/所有）
        :return:
        """
        # 把对象转换成python的字典格式。
        plan_id = request.args.get("id")
        logger.info(f"接收到的参数 <===== {plan_id}")
        if plan_id:
            # 保持接口返回信息，数据格式一致，这样前端调用比较方便
            plan_datas = [plan_service.get(plan_id).as_dict()]
        else:
            datas = plan_service.get_list()
            # 拿到所有的计划数据，返回给前端显示
            plan_datas = [data.as_dict() for data in datas]
        return {"code": 0, "msg": {"data": plan_datas}}

    post_paresr = api.parser()
    post_paresr.add_argument("name", type=str, required=True, location="json")
    post_paresr.add_argument("testcase_ids", type=str, location="json")

    @plan_ns.expect(post_paresr)
    def post(self):
        """
        新增测试计划
        :return:
        """
        # 获取请求数据
        req_data = request.json
        # 获取service 层需要的测试用例的 id 列表 [1,2]
        testcase_id_list = req_data.get("testcase_ids")
        # 原因： 获取到的内容是str，期望是list
        # 解决方案： 从接口如果传过来是一个string，那么就转换成想要的list结构
        if isinstance(testcase_id_list, str):
            testcase_id_list = json.loads(testcase_id_list)
        plan_name = req_data.get("name")  # 拿到计划名称
        plan_entity = PlanEntity(name=plan_name)  # 根据计划名称拿到实体
        # 保存
        res = plan_service.save(plan_entity, testcase_id_list)
        if res:
            return {"code": 0, "msg": f"plan id {res} success add."}
        else:
            return {"code": 40001, "msg": "plan is exists"}
