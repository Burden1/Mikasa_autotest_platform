"""
    构建记录Service层
"""
from dao.build_dao import BuildDao
from do.build_entity import BuildEntity

build_dao = BuildDao()


class BuildService:
    def save(self, build_entity: BuildEntity):
        """
        新增构建记录
        :param build_entity: 构建记录实体
        :return:
        """
        return build_dao.save(build_entity)

    def get_list_by_plan_id(self, plan_id):
        """
        根据计划id查询构建记录
        :param plan_id: 计划id
        :return:
        """
        return build_dao.get_list_by_plan_id(plan_id)
