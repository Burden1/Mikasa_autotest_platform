"""
    单元测试类：pytest
"""
from do.testcase_entity import TestCaseEntity
from service.testcase_service import TestcaseService


class TestTestcaseSerivce:
    def setup_class(self):
        self.testcase_service = TestcaseService()

    def test_save(self):
        testcase_entity = TestCaseEntity(case_title="test_demo1.py", remark="备注1")
        print(self.testcase_service.save(testcase_entity))

    def test_get(self):
        print(self.testcase_service.get(1))

    def test_get_list(self):
        print(self.testcase_service.get_list())

    def test_update(self):
        testcase_entity = TestCaseEntity(id=5, case_title="test_demo修改.py", remark="修改信息")
        self.testcase_service.update(testcase_entity)

    def test_delete(self):
        self.testcase_service.delete(2)
