
# 获取driver
from base.get_driver import get_driver
from page.page_login import PageLogin

driver = get_driver()
class PageIn():
    def page_get_pagelogin(self):
        return PageLogin(driver)