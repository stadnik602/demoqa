from selene import browser, have

from demoqa.steps.simple_user_registration_steps import SimpleUserRegistrationSteps


class Sidebar:
    def __init__(self):
        self.container = browser.element(".left-pannel")
        self.category = browser.all(".left-pannel .header-text")
        self.page = browser.all(".left-pannel li span")

    def open_category(self, item):
        self.category.element_by(have.exact_text(item)).click()
        return self

    def open_page(self, page):
        self.page.element_by(have.exact_text(page)).click()

    def open_simple_registration_page(self):
        self.open_category("Elements")
        self.open_page("Text Box")
        return SimpleUserRegistrationSteps()
