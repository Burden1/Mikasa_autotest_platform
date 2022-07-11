"""
    该类为jenkins工具类
"""

# 获取Jenkins的版本
from jenkinsapi.jenkins import Jenkins


class JenkinsUtils:
    # Jenkins 服务
    BASE_URL = "http://www.loseweight.ren:8080/"
    # Jenkins 服务对应的用户名
    USERNAME = "admin"
    # Jenkins 服务对应的token
    PASSWORD = "117b61c7fa8273bac9310916dc65277ac7"
    JOB = "ck22"

    @classmethod
    def invoke(cls, testcase_info):
        # 1、连接jenkins
        mikasa_jenkins = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        # 2、获取Jenkins 的job 对象
        job = mikasa_jenkins.get_job(cls.JOB)
        # 3、构建hogwarts job， 传入的值必须是字典， key 对应 jenkins 设置的参数名
        job.invoke(build_params={"task": testcase_info})
        # 4、拿到当前构建记录，即最后一次构建记录+1
        last_number = job.get_last_buildnumber() + 1
        # 5、拼接测试报告地址： http://www.mikasa.com:8080/job/mikasa2/14/allure/
        report_url = f"{cls.BASE_URL}job/{cls.JOB}/{last_number}/allure"
        return report_url
