import allure
from selene import browser

from demoqa.data import users


@allure.tag("web")
@allure.severity(allure.severity_level.CRITICAL)
@allure.step("Registration simple user")
@allure.label("owner", "k.stadnyk")
@allure.feature("Simple registration form")
@allure.story("The user can be registered by filling the simple registration form")
def test_registers_user(app):
    user = users.simple_user
    app.open().open_sidebar().open_simple_registration_page().register(
        user
    ).should_have_data(user)
