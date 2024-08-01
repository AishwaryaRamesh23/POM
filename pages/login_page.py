from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_credentials(self, email: str, password: str):
        # Fill in the email and password fields
        self.page.get_by_label("Your username or email").fill(email)
        self.page.get_by_label("Your password").fill(password)

    def submit_login(self):
        # Click the login button
        login_button = self.page.locator('//*[@id="content"]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/form/div[3]/button')
        login_button.click()
        # Wait for network idle to ensure the login process completes
        self.page.wait_for_load_state('networkidle')