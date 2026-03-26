from selene import browser

from demoqa.components.sidebar import Sidebar
from demoqa.pages.registration_page import RegistrationPage
from demoqa.steps.simple_user_registration_steps import (
    SimpleUserRegistrationPage,
    SimpleUserRegistrationSteps,
)
from demoqa.steps.registration_steps import UserRegistrationSteps


class Application:
    def __init__(self):
        self.simple_registration_page = SimpleUserRegistrationPage()
        self.simple_registration_steps = SimpleUserRegistrationSteps()
        self.registration_page = RegistrationPage()
        self.user_registration_steps = UserRegistrationSteps()
        self.sidebar = Sidebar()

    def open(self):
        browser.open("/")
        return self

    def open_sidebar(self):
        browser.all(".category-cards a")[1].click()
        return Sidebar()
