from selene import browser, have


class SimpleUserRegistrationPage:
    def __init__(self):
        self.full_name = browser.element("#userName")
        self.email = browser.element("#userEmail")
        self.current_address = browser.element("#currentAddress")
        self.submit_button = browser.element("#submit")

    def open(self):
        browser.open("https://demoqa.com/text-box")

    def fill_full_name(self, value):
        self.full_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def submit(self):
        self.submit_button.click()

    def should_have_submitted(self, full_name, email):
        browser.all("#output p").should(have.texts(full_name, email))
