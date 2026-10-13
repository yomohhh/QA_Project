from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)


        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")

        self.login_button = page.get_by_role("button", name="Login")

        self.error_message = page.locator("[data-test='error']")


    def login_to_shop(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
