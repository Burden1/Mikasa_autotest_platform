"""
    测试计划实体类
"""
from sqlalchemy import *
from sqlalchemy.orm import relationship

from do.testcase_plan_rel import testcase_plan_rel
from app import db


class PlanEntity(db.Model):
    # 表名
    __tablename__ = "plan"
    # 用例ID 用例的唯 一标识
    id = db.Column(Integer, primary_key=True)
    # 用例的标题 或者文件名,限定 80个字符 ，不为空，并且唯一
    name = db.Column(String(80), nullable=False, unique=True)
    # 反射，和测试用例实体进行一个关联
    testcases = relationship("TestCaseEntity",
                             secondary=testcase_plan_rel)

    def as_dict(self):
        # [TestcaseEntity<1>] => test_demo.py testcase_2.py
        return {"id": self.id, "name": self.name,
                # 遍历拿到测试用例名称，并且将名称转为字符串格式
                "testcase_info": " ".join([testcase.case_title for testcase in self.testcases])}
