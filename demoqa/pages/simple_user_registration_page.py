from selene import browser


class SimpleUserRegistrationPage:
    def __init__(self):
        self.url = "https://demoqa.com/text-box"
        self.full_name = browser.element("#userName")
        self.email = browser.element("#userEmail")
        self.current_address = browser.element("#currentAddress")
        self.submit_button = browser.element("#submit")

    def fill_full_name(self, value):
        self.full_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def fill_current_address(self, value):
        self.current_address.type(value)
        return self

    def submit(self):
        self.submit_button.click()


"""        browser.all("#output p").should(
            have.texts(user.full_name, user.email, user.current_address)
        )"""
