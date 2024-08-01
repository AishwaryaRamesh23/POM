from playwright.sync_api import Page

class MainPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_login(self):
        # Wait for and click the "Log in" button
        self.page.wait_for_selector('text="Log in"')
        self.page.click('text="Log in"')

    def click_developer_login(self):
        # Wait for and click the "Developer Login" link
        dev_login_locator = self.page.locator('//*[@id="main"]/article/div/div/div/ul/li[2]/p[2]/a')
        dev_login_locator.click()