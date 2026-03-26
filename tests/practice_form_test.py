import allure

from demoqa.data import users


@allure.tag("web")
@allure.severity(allure.severity_level.BLOCKER)
@allure.step("Register user with user's data")
@allure.label("owner", "k.stadnyk")
@allure.feature("Registration")
@allure.story("The user can be registered by filling the registration form")
@allure.link(
    "https://demoqa.com/automation-practice-form", name="Automation practice form"
)
def test_successes_submit_form_by_page_object_steps(app):
    user = users.user
    (
        app.user_registration_steps.open()
        .register(user)
        .should_confirmation_popup_title("Thanks for submitting the form")
        .should_have_registered_user_data(user)
    )
