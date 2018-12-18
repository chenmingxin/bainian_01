import os
import sys

import allure

sys.path.append(os.getcwd())

from base.read_yaml import ReadYaml
import pytest
from page.page_in import PageIn
from page.page_login import PageLogin

def get_data():
    arrs = []
    for data in ReadYaml("login_data.yaml").read_yaml().values():
        arrs.append((data.get("username"),data.get("pwd"),data.get("expect_result"),data.get("expect_toast")))
    return arrs

class TestLogin():
    def setup_class(self):
        self.test = PageIn().page_get_pagelogin()
        # 点击我
        self.test.page_click_me()
        # 已有账号去登录
        self.test.page_click_dl()

    def teardown_class(self):
        self.test.driver.quit()

    @pytest.mark.parametrize("username,pwd,expect_result,expect_toast",get_data())
    @allure.step("测试步骤")
    def test_login(self,username,pwd,expect_result,expect_toast):
        test = self.test
        if expect_result:
            try:
                # 输入用户名
                test.page_login_input_username(username)
                # 输入密码
                test.page_login_input_pwd(pwd)
                # 点击登录
                test.page_login_click()
                # 断言
                assert expect_result in test.page_get_nickname()
                # 点击设置
                test.page_click_setting()
                # 滑动并退出
                test.logout()
                # 点击我
                test.page_click_me()
                # 点击登录
                test.page_click_dl()
            except AssertionError:
                self.test.base_get_img()
                raise
        else:
            try:
                # 输入用户名
                test.page_login_input_username(username)
                # 输入密码
                test.page_login_input_pwd(pwd)
                # 点击登录
                test.page_login_click()
                assert "用户不存在哦" in test.base_get_toast(expect_toast)
            except AssertionError:
                self.test.base_get_img()
                with open("./image/faild.png","rb") as f:
                    allure.attach("失败原因: ",f.read(),allure.attach_type.PNG)
                raise









