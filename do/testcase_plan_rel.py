"""
    测试用例_测试计划_中间表 实体类
"""
from sqlalchemy import *

from app import db

testcase_plan_rel = db.Table(
    'testcase_plan_rel',
    Column('testcase_id', Integer,
           ForeignKey('testcase.id'),
           primary_key=True),
    Column('plan_id', Integer,
           ForeignKey('plan.id'),
           primary_key=True))
