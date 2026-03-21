from selene import browser

from demoqa.data import users
from demoqa.pages.simple_user_registration_page import SimpleUserRegistrationPage


def test_registers_user():
    registration_page = SimpleUserRegistrationPage()

    user = users.simple_user

    registration_page.open().fill_form(user).submit().should_have_data(user)
