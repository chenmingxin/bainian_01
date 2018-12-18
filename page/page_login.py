import allure

import page
from base.base import Base
# 登录页面封装
class PageLogin(Base):
    # 单击 我
    @allure.step("点击我")
    def page_click_me(self):
        self.base_click(page.login_click_me)
        # 点击已有账号登录
    @allure.step("点击已有账号登录")
    def page_click_dl(self):
        self.base_click(page.login_click_dl)
    # 输入用户名
    @allure.step("点击已有账号登录")
    def page_login_input_username(self,username):
        self.base_input(page.login_username,username)

    @allure.step("输入密码")
    def page_login_input_pwd(self,pwd):
        self.base_input(page.login_pwd,pwd)

    @allure.step("点击登录")
    def page_login_click(self):
        self.base_click(page.login_click)

    @allure.step("获取昵称")
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)

    @allure.step("点击设置")
    def page_click_setting(self):
        self.base_click(page.login_click_setting)

    @allure.step("获取截图")
    def page_get_image(self):
        self.base_get_img()

    @allure.step("拖拽")
    def page_drag_and_drop(self):
        el1=self.base_find_element(page.login_msg_send)
        el2=self.base_find_element(page.login_update_pwd)
        self.base_drag_and_drop(el1,el2)

    @allure.step("点击退出")
    def page_exit(self):
        self.base_click(page.login_exit)

    @allure.step("确认退出")
    def page_logout(self):
        self.base_click(page.login_logout)


# 封装拖拽及退出
    def logout(self):
        self.page_drag_and_drop()
        self.page_exit()
        self.page_logout()

    # def page_get_toast(self,msg):
    #     self.base_get_toast(msg)
