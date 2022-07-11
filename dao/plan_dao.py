"""
    测试计划Dao层
"""
from do.plan_enetity import PlanEntity

from app import db_session


class PlanDao:
    def save(self, plan_entity: PlanEntity):
        """
        新增测试计划
        :param plan_entity: 计划orm对象
        :return:
        """
        db_session.add(plan_entity)
        db_session.commit()
        # 在数据提交之后再获取一下
        plan_id = plan_entity.id
        db_session.close()
        return plan_id

    def get(self, plan_id):
        """
        根据计划id查询单个测试计划
        :param plan_id: 计划id
        :return:
        """
        return db_session.query(PlanEntity).filter_by(id=plan_id).first()

    def get_list(self):
        """
        查询所有测试计划
        :return:
        """
        return db_session.query(PlanEntity).all()
