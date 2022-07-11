"""
    测试用例实体类
"""
from sqlalchemy import *
from app import db


class TestCaseEntity(db.Model):
    # 表名
    __tablename__ = "testcase"
    # 用例ID 用例的唯 一标识
    id = db.Column(Integer, primary_key=True)
    # 用例的标题 或者文件名,限定 80个字符 ，不为空，并且唯一
    case_title = db.Column(String(80), nullable=False, unique=True)
    # 备注
    remark = db.Column(String(120))

    def as_dict(self):
        return {"id": self.id, "case_title": self.case_title, "remark": self.remark}
