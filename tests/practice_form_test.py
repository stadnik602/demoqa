from demoqa.data import users


def test_successes_submit_form_by_page_object_steps(app):
    user = users.user
    (
        app.user_registration_steps.open()
        .register(user)
        .should_confirmation_popup_title("Thanks for submitting the form")
        .should_have_registered_user_data(user)
    )
