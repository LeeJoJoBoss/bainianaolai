import page

from base.base_act import Base


class PageLogin(Base):
    #点击我
    def page_me(self):
        self.base_click(page.login_me)

    #点击已有账号，去登录
    def page_me_exists(self):
        self.base_click(page.login_user_exists)

    #输入账号
    def page_input_user(self,username):
        self.base_input(page.login_user,username)

    #输入密码
    def page_input_password(self,pwd):
        self.base_input(page.login_password,pwd)

    #点击登录
    def page_go(self):
        self.base_click(page.login_go)

    #获取登录后文本
    def page_text(self):
        return self.base_get_text(page.login_text)

    #点击设置
    def page_setting(self):
        self.base_click(page.login_setting)

    #进行拖拽
    def page_move(self):
        picture=self.base_find_element(page.login_picture)
        change=self.base_find_element(page.login_change_password)
        self.base_drag_and_drop(picture,change)

    #点击退出
    def page_out(self):
        self.base_click(page.login_out)

    #点击确认退出
    def page_againout(self):
        self.base_click(page.login_againout)


    #将页面登录的操作流程封装进一个方法可以直接一次性调用
    def page_login(self,username,pwd):
        self.page_me()
        self.page_me_exists()
        self.page_input_user(username)
        self.page_input_password(pwd)
        self.page_go()

    # 将页面退出的操作流程封装进一个方法可以直接一次性调用
    def page_userout(self):
        self.page_setting()
        self.page_move()
        self.page_out()
        self.page_againout()