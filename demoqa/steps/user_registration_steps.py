import calendar

from selene import browser, have

from demoqa.data.users import UserPractiseForm
from demoqa.pages.registration_page import RegistrationPage, Hobbies

confirmation_popup_title_element = browser.element("#example-modal-sizes-title-lg")

class UserRegistrationSteps:
    def __init__(self):
        self.page = RegistrationPage()

    def open(self):
        self.page.open()
        return self

    def register(self, user: UserPractiseForm):
        (
        self.page
         .fill_first_name(user.first_name)
         .fill_last_name(user.last_name)
         .fill_email(user.email)
         .click_gender_radiobutton(user.gender)
         .fill_mobile(user.mobile)
         .fill_date_of_birth(user.date_of_birth)
         .select_subject(user.subjects)
         .select_hobby(Hobbies.MUSIC)
         .chose_picture(user.picture)
         .fill_current_address(user.address)
         .fill_state_and_city(user.state, user.city)
         .click_submit_button()
         )
        return self

    def should_be_displayed_user_registered_data(self, user: UserPractiseForm):
        # формируем список всех ячеек таблицы (заголовки + значения)
        expected_values = [
            "Student Name", f"{user.first_name} {user.last_name}",
            "Student Email", user.email,
            "Gender", user.gender,
            "Mobile", user.mobile,
            "Date of Birth", f"{user.date_of_birth.day} {calendar.month_name[user.date_of_birth.month]},{user.date_of_birth.year}",
            "Subjects", ", ".join(user.subjects),
            "Hobbies", ", ".join([h.value for h in user.hobbies]),
            "Picture", user.picture,
            "Address", user.address,
            "State and City", f"{user.state} {user.city}",
        ]

        # проверяем все td подряд
        browser.element(".table").all("td").should(have.texts(*expected_values))
        return self

    def should_confirmation_popup_title(self, title):
        confirmation_popup_title_element.should(have.exact_text(title))
        return self


