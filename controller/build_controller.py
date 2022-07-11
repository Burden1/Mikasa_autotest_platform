"""
    构建记录控制层
"""
from flask import request
from flask_restx import Namespace, Resource

from app import api
from do import BuildEntity
from service.build_service import BuildService
from utils.log_utils import logger

build_ns = Namespace("build", description="构建记录管理")
build_service = BuildService()


@build_ns.route("")
class BuildController(Resource):
    get_paresr = api.parser()
    # 查看的是某个测试计划的构建记录
    get_paresr.add_argument("plan_id", type=int, location="args")

    @build_ns.expect(get_paresr)
    def get(self):
        """
        根据测试计划id查询构建记录(单个/所有)
        :return:
        """
        # 把对象转换成python的字典格式。
        plan_id = request.args.get("plan_id")
        logger.info(f"获取构建记录通过测试计划ID<===== {plan_id}")
        if plan_id:
            build_res = build_service.get_list_by_plan_id(plan_id)
            res = [build.as_dict() for build in build_res]
            return {"code": 0, "msg": {"data": res}}
        else:
            return {"code": 40005, "msg": "plan_id is not exist"}

    post_paresr = api.parser()
    post_paresr.add_argument("id", type=int, required=True, location="json")
    post_paresr.add_argument("plan_id", type=int, required=True, location="json")
    post_paresr.add_argument("report", type=str, location="json")
    post_paresr.add_argument("create_time", location="json")

    @build_ns.expect(post_paresr)
    def post(self):
        """
        新增构建记录
        :return:
        """
        # 获取请求数据
        case_data = request.json
        build_entity = BuildEntity(**case_data)
        res = build_service.save(build_entity)
        if res:
            return {"code": 0, "msg": f"case id {res} success add."}
        else:
            return {"code": 40001, "msg": "buildId is exists"}
