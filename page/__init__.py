from selenium.webdriver.common.by import By
# 点击我
login_click_me =By.XPATH,"//*[contains(@text,'我')]"
# 已有账号,去登录
login_click_dl = By.ID,"com.yunmall.lc:id/textView1"
# 输入用户名
login_username = By.ID,"com.yunmall.lc:id/logon_account_textview"
# 输入密码
login_pwd = By.ID,"com.yunmall.lc:id/logon_password_textview"
# 点击登录
login_click = By.ID,"com.yunmall.lc:id/logonContent"
# 昵称
login_nickname = By.ID,"com.yunmall.lc:id/tv_user_nikename"
# 点击设置
login_click_setting = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 消息推送--点击
login_msg_send = By.ID,"com.yunmall.lc:id/setting_notification"
# 修改密码
login_update_pwd = By.ID,"com.yunmall.lc:id/setting_modify_pwd"
# 退出
login_exit = By.ID,"com.yunmall.lc:id/setting_logout"
# 确认
login_logout = By.ID,"com.yunmall.lc:id/ymdialog_right_button"