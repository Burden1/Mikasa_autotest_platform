"""
    测试计划测试用例类
    框架：pytest
"""
from do.plan_enetity import PlanEntity
from service.plan_serivce import PlanService


class TestPlanService:
    def setup_class(self):
        self.plan_service = PlanService()

    def test_save(self):
        plan_entity = PlanEntity(name="测试计划3")
        self.plan_service.save(plan_entity, [5, 6])

    def test_get(self):
        print(self.plan_service.get(1))

    def test_get_list(self):
        print(self.plan_service.get_list())

    def test_execute(self):
        self.plan_service.execute("测试用例信息", 1)
