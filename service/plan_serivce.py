"""
    测试计划业务层
"""
from typing import List

from dao.plan_dao import PlanDao
from do.build_entity import BuildEntity
from do.plan_enetity import PlanEntity
from service import build_service
from service.testcase_service import TestcaseService
from utils.jenkins_utils import JenkinsUtils
from utils.log_utils import logger
from service.build_service import BuildService

plan_dao = PlanDao()
testcase_service = TestcaseService()
build_service = BuildService()


class PlanService:
    def save(self, plan_entity: PlanEntity, testcase_id_list: List[int]):
        """
        添加测试计划
        :return:
        """
        logger.debug(f"测试计划关联的用例id为{type(testcase_id_list)}")
        # 因为我们需求页面需要勾选多个测试用例，然后进行生成计划，所以我们会在这里接收一个idlist
        # 1、遍历id列表，然后根据id拿到对应的测试用例对象
        testcase_objs = [testcase_service.get(testcase_id) for testcase_id in testcase_id_list]
        logger.debug(f"测试计划关联的用例对象为{testcase_objs}")

        # 2、遍历拿取各个测试用例的标题，之后我们调用jenkins的时候是要用标题名称来调用的
        testcase_title_list = [testcase_obj.case_title for testcase_obj in testcase_objs]
        logger.debug(f"测试计划获取到的测试用例的标题为{testcase_title_list}")

        # 3、测试计划关联对应的测试用例对象
        plan_entity.testcases = testcase_objs
        # 4、保存，并拿到测试计划id
        plan_id = plan_dao.save(plan_entity)
        # 5、执行测试计划
        return self.execute(testcase_title_list, plan_id)

    def get(self, plan_id) -> PlanEntity:
        """
            查询单个测试计划
        """
        return plan_dao.get(plan_id)

    def get_list(self) -> List[PlanEntity]:
        """
            查询全部测试计划
        """
        return plan_dao.get_list()

    def execute(self, testcase_title_list, plan_id):
        """
        执行测试计划：结合jenkins执行测试用例,并拿到执行报告结果
        :param testcase_title_list: 测试用例标题集合，主要为了执行
        :param plan_id: 测试计划id
        :return:
        """
        # ['test_demo1.py', 'test_demo2.py']  -> test_demo1.py test_demo2.py
        # 1、用例标题列表转换为字符串
        testcase_titles = " ".join(testcase_title_list)
        logger.debug(f"需要执行的用例为{testcase_titles}")

        # 2、调用Jenkins
        report = JenkinsUtils.invoke(testcase_titles)
        logger.debug(f"测试报告地址:{report}")
        # 3、创建构建记录的实例
        build_entity = BuildEntity(plan_id=plan_id, report=report)
        # 4、新增一条构建记录
        return build_service.save(build_entity)
