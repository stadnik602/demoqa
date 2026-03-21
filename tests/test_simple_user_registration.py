from selene import browser

from demoqa.data import users
from demoqa.steps.simple_user_registration_steps import SimpleUserRegistrationSteps


def test_registers_user():
    registration_page = SimpleUserRegistrationSteps()

    user = users.simple_user

    (registration_page.open().register(user).should_have_data(user))
