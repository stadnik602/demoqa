from selene import browser, have

from demoqa.data.users import TestUser


class SimpleUserRegistrationPage:
    def __init__(self):
        self.full_name = browser.element("#userName")
        self.email = browser.element("#userEmail")
        self.current_address = browser.element("#currentAddress")
        self.submit_button = browser.element("#submit")

    def open(self):
        browser.open("https://demoqa.com/text-box")
        return self

    def fill_form(self, user: TestUser):
        self.full_name.type(user.full_name)
        self.email.type(user.email)
        self.current_address.type(user.current_address)
        return self

    def submit(self):
        self.submit_button.click()
        return self

    def should_have_submitted(self, full_name, email, current_address):
        browser.all("#output p").should(have.texts(full_name, email, current_address))
