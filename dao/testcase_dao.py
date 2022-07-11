"""
    测试用例dao层
    专门处理与数据库相关的操作
"""
from do.testcase_entity import TestCaseEntity
from app import db_session


class TestcaseDao:
    def save(self, testcase_entity: TestCaseEntity):
        """
        新增测试用例
        :return:
        """
        db_session.add(testcase_entity)
        db_session.commit()
        case_id = testcase_entity.id
        db_session.close()
        return case_id

    def get(self, case_id):
        """
        根据用例id查询测试用例
        :return:
        """
        return db_session.query(TestCaseEntity).filter_by(id=case_id).first()

    def get_list(self):
        """
        查询所有用例
        :return:
        """
        return db_session.query(TestCaseEntity).all()

    def update(self, testcase_entity: TestCaseEntity):
        """
        更新用例
        :return:
        """
        db_session.commit()
        # 在数据提交之后再获取一下
        testcase_id = testcase_entity.id
        db_session.close()
        return testcase_id

    def delete(self, testcase_entity):
        """
        删除测试用例
        :param testcase_entity:
        :return:
        """
        db_session.delete(testcase_entity)
        db_session.commit()
        db_session.close()
