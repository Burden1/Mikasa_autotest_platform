"""
    构建记录测试用例层
    框架：pytest
"""
from do import BuildEntity
from service.build_service import BuildService


class TestBuildService:
    def setup_class(self):
        self.build_service = BuildService()

    def test_save(self):
        build_entity = BuildEntity(plan_id=1, report="test_demo1.py")
        return self.build_service.save(build_entity)

    def test_get_list_by_plan_id(self):
        print(self.build_service.get_list_by_plan_id(1))
