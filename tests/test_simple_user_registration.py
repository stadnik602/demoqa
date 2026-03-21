from selene import browser

from demoqa.pages.simple_user_registration_page import SimpleUserRegistrationPage


def test_registers_user():
    registration_page = SimpleUserRegistrationPage()

    registration_page.open()

    registration_page.fill_full_name("Bobr Kurva")
    registration_page.fill_email("bkurva@gmail.com")
    registration_page.submit()
    registration_page.should_have_submitted("Bobr Kurva", "bkurva@gmail.com")
