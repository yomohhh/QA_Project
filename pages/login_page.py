from pages.base_page import BasePage


# Создаем класс LoginPage, который наследует (забирает методы) у BasePage
class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)  # Передаем вкладку браузера в родительский класс

        # Описываем локаторы (карту элементов страницы)
        # get_by_placeholder ищет поле по серой подсказке внутри него
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")

        # get_by_role ищет конкретно кнопку с текстом "Login"
        self.login_button = page.get_by_role("button", name="Login")

        # locator использует технический селектор для поиска всплывающей ошибки
        self.error_message = page.locator("[data-test='error']")

    # Объединяем шаги в одно пользовательское действие — логин
    def login_to_shop(self, username, password):
        self.username_input.fill(username)  # Напечатать логин
        self.password_input.fill(password)  # Напечатать пароль
        self.login_button.click()  # Кликнуть на кнопку входа
