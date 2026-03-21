from selene import browser, have

from demoqa.data.users import User
from demoqa.pages.simple_user_registration_page import SimpleUserRegistrationPage


class SimpleUserRegistrationSteps:
    def __init__(self):
        self.page = SimpleUserRegistrationPage()

    def open(self):
        browser.open(self.page.url)
        return self

    def register(self, user: User):
        (
            self.page.fill_full_name(user.full_name)
            .fill_email(user.email)
            .fill_current_address(user.current_address)
            .submit()
        )
        return self

    def should_have_data(self, user):
        browser.element("#output #name").should(have.text(user.full_name))
        browser.element("#output #email").should(have.text(user.email))
        browser.element("#output #currentAddress").should(
            have.text(user.current_address)
        )
