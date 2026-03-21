from selene import browser

from demoqa.data import users
from demoqa.pages.application import app


def test_registers_user():
    user = users.simple_user
    # app.simple_registration_steps.open().register(user).should_have_data(user)
    app.open().open_sidebar().open_simple_registration_page().register(
        user
    ).should_have_data(user)
