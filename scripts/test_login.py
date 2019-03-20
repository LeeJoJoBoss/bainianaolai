import sys
import os
sys.path.append(os.getcwd())
from page.page_login import PageLogin


from base.base_appstart import appStart



class TestLogin:
    def setup(self):
        self.app=appStart()
        self.AppLogin=PageLogin(self.app)

    def teardown(self):
        self.app.quit()

    def test01(self,user='itheima',pwd='123456',expect_result="itheima"):
        self.AppLogin.page_login(user, pwd)
        self.AppLogin.page_userout()
        # try:
        #     # 断言
        #     print(self.AppLogin.page_text())
        #     assert expect_result == self.AppLogin.page_text()
        #     try:
        #         # 退出
        #         self.AppLogin.page_out()
        #         # 断言退出是否成功
        #         assert self.AppLogin.page_userout()
        #     except:
        #         print("退出断言失败")
        # except AssertionError as e:
        #     print("登录断言出错！")

#关于生成测试报告addopts = -s --html=./report/report_login.html
#生成在线测试报告alluredir serve reportur