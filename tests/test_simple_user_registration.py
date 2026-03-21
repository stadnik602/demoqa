from selene import browser

from demoqa.data.users import TestUser
from demoqa.pages.simple_user_registration_page import SimpleUserRegistrationPage


def test_registers_user():
    registration_page = SimpleUserRegistrationPage()

    bobr_user = TestUser(
        full_name="Bobr Kurva",
        email="bkurva@gmail.com",
        current_address="Dunsheath Way 777, MArkham, ON",
    )

    registration_page.open().fill_form(bobr_user).submit()

    registration_page.should_have_submitted(
        bobr_user.full_name, bobr_user.email, bobr_user.current_address
    )
