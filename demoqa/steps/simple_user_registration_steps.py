import allure
from selene import browser, have

from demoqa.data.users import User
from demoqa.pages.simple_user_registration_page import SimpleUserRegistrationPage


class SimpleUserRegistrationSteps:
    def __init__(self):
        self.page = SimpleUserRegistrationPage()

    @allure.step("Open the simple registration page")
    def open(self):
        browser.open(self.page.url)
        return self

    @allure.step("Fill user data in the form's fields")
    def register(self, user: User):
        (
            self.page.fill_full_name(user.full_name)
            .fill_email(user.email)
            .fill_current_address(user.current_address)
            .submit()
        )
        return self

    @allure.step("The entered user's data are displayed")
    def should_have_data(self, user):
        with allure.step(f"The user's full_name is displayed: {user.full_name}"):
            browser.element("#output #name").should(have.text(user.full_name))
        with allure.step(f"The user's email is displayed: {user.email} "):
            browser.element("#output #email").should(have.text(user.email))
        with allure.step(
            f"The user's current address is displayed: {user.current_address}"
        ):
            browser.element("#output #currentAddress").should(
                have.text(user.current_address)
            )
