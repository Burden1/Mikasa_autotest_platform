"""
    测试用例业务层
"""
from typing import List

from dao.testcase_dao import TestcaseDao
from do.testcase_entity import TestCaseEntity
from utils.log_utils import logger

testcase_dao = TestcaseDao()


class TestcaseService:
    def save(self, testcase_entity: TestCaseEntity):
        """
        新增测试用例
        :return:
        """
        # 如果用例不存在才进行添加
        res = self.get(testcase_entity.id)
        if res:
            logger.info("测试用例已存在，不能进行添加")
            return False
        else:
            # 用例id不存在，调用dao层，对数据库进行添加操作
            return testcase_dao.save(testcase_entity)

    def get(self, case_id) -> TestCaseEntity:
        """
        根据用例id查询测试用例
        :return:
        """
        return testcase_dao.get(case_id)

    def get_list(self) -> List[TestCaseEntity]:
        """
        查询所有用例
        :return:
        """
        return testcase_dao.get_list()

    def update(self, testcase_entity: TestCaseEntity):
        """
        更新用例
        :return:
        """
        # 如果用例存在才进行更新
        print("要修改的用例id:", testcase_entity.id)
        res = self.get(testcase_entity.id)
        if res:
            res.case_title = testcase_entity.case_title
            res.remark = testcase_entity.remark
            return testcase_dao.update(res)
        else:
            logger.info("测试用例不存在，不能进行更新")
            return False

    def delete(self, case_id):
        """
        删除测试用例
        :param case_id:
        :return:
        """
        res = self.get(case_id)
        if res:
            testcase_dao.delete(res)
            return res
        else:
            logger.info("测试用例不存在，不能进行删除")
            return False
