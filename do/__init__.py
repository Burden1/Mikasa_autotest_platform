"""
    数据库表创建
    注意：创建一次后，就可以注释掉，避免之后每次启动项目都创建
"""
from do.build_entity import BuildEntity
from do.plan_enetity import PlanEntity
from do.testcase_plan_rel import testcase_plan_rel
from app import db
from do.testcase_entity import TestCaseEntity

if __name__ == '__main__':
    db.create_all()
