import allure
from selene import browser, have

from demoqa.data.users import UserPractiseForm
from demoqa.pages.registration_page import RegistrationPage, Hobby


class UserRegistrationSteps:
    def __init__(self):
        self.page = RegistrationPage()
        self.registered_user_data_table = browser.element(".table").all("td")
        self.confirmation_popup_title_element = browser.element(
            "#example-modal-sizes-title-lg"
        )

    @allure.step("Opening registration form")
    def open(self):
        self.page.open()
        return self

    @allure.step("Register user")
    def register(self, user: UserPractiseForm):
        (
            self.page.fill_first_name(user.first_name)
            .fill_last_name(user.last_name)
            .fill_email(user.email)
            .click_gender_radiobutton(user.gender)
            .fill_mobile(user.mobile)
            .fill_date_of_birth(user.date_of_birth)
            .select_subject(user.subjects)
            .select_hobby(user.hobbies)
            .chose_picture(user.picture)
            .fill_current_address(user.address)
            .fill_state_and_city(user.state, user.city)
            .click_submit_button()
        )
        return self

    @allure.step("Verifying user data in the table")
    def should_have_registered_user_data(self, user: UserPractiseForm):
        expected_values = [
            "Student Name",
            f"{user.first_name} {user.last_name}",
            "Student Email",
            user.email,
            "Gender",
            user.gender.value,
            "Mobile",
            user.mobile,
            "Date of Birth",
            f"{user.date_of_birth.strftime('%d %B,%Y')}",
            "Subjects",
            ", ".join(s.value for s in user.subjects),
            "Hobbies",
            ", ".join([h.value for h in user.hobbies]),
            "Picture",
            user.picture,
            "Address",
            user.address,
            "State and City",
            f"{user.state} {user.city}",
        ]

        self.registered_user_data_table.should(have.texts(*expected_values))
        return self

    @allure.step("Verify title of the user data popup")
    def should_confirmation_popup_title(self, title):
        self.confirmation_popup_title_element.should(have.exact_text(title))
        return self
