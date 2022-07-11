"""
    构建记录dao层
"""

from typing import List

from do.build_entity import BuildEntity
from app import db_session


class BuildDao:
    def save(self, build_entity: BuildEntity):
        """
        新增构建记录
        :param build_entity:
        :return:
        """
        db_session.add(build_entity)
        db_session.commit()
        # 在数据提交之后再获取一下
        build_id = build_entity.id
        print("build_id：", build_id)
        db_session.close()
        return build_id

    def get_list_by_plan_id(self, plan_id) -> List[BuildEntity]:
        """
        根据计划id查询所有构建记录
        :param plan_id:
        :return:
        """
        return db_session.query(BuildEntity).filter_by(plan_id=plan_id).all()
