"""
    构建记录实体类
"""
from datetime import datetime

from sqlalchemy import *

from app import db


class BuildEntity(db.Model):
    # 表名
    __tablename__ = "build"
    # 用例ID 用例的唯 一标识
    id = db.Column(Integer, primary_key=True)
    # 是一个plan的外键
    plan_id = db.Column(Integer, ForeignKey('plan.id'))
    # 用例的标题 或者文件名,限定 80个字符 ，不为空，并且唯一
    report = db.Column(String(80), nullable=False)
    # 创建时间，由orm自动生成，无需实例化的时候传参
    create_time = Column(DateTime, nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def as_dict(self):
        # 问题： Object of type datetime is not JSON serializable
        # 解决方案：
        return {"plan_id": self.plan_id,
                "report": self.report,
                "create_time": str(self.create_time)}
