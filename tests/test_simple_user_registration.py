from selene import browser

from demoqa.data import users


def test_registers_user(app):
    user = users.simple_user
    app.open().open_sidebar().open_simple_registration_page().register(
        user
    ).should_have_data(user)
