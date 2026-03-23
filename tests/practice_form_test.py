from selene import browser, have, command

from demoqa.data.users import UserPractiseForm
from demoqa.pages.registration_page import (
    RegistrationPage,
    confirmation_popup_title_element, Hobbies,
)
from demoqa.steps.user_registration_steps import UserRegistrationSteps
from demoqa.data import users

def test_successes_submit_form_by_page_object_steps():
    user = users.user
    page = UserRegistrationSteps()
    (page
     .open()
     .register(user)
     .should_confirmation_popup_title("Thanks for submitting the form")
     .should_be_displayed_user_registered_data(user)
    )
