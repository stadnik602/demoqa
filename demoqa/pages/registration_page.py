from selene import browser

from demoqa import resource
from tests.practice_form_test import (
    FORM_PAGE_URL,
    first_name_field,
    last_name_field,
    date_of_birth_field,
    datepicker,
    email_field,
    gender_radiobuttons,
    mobile_field,
    subject_input,
    hobbies_checkboxes,
    choose_picture_button,
    current_address_input,
    state_input,
    city_input,
)


class RegistrationPage:
    def __init__(self):
        self.registered_user_data = browser.all(".table").all("td")

    def open(self):
        browser.open(FORM_PAGE_URL)

    def fill_first_name(self, value):
        first_name_field.type(f"{value}")

    def fill_last_name(self, last_name):
        last_name_field.type(f"{last_name}")

    def fill_date_of_birth(self, year, month, day):
        date_of_birth_field.click()
        datepicker.get("year_dropdown").send_keys(year)
        datepicker.get("month_dropdown").send_keys(month)
        browser.element(f".react-datepicker__day--0{day}").click()

    """    def should_registered_user_with(self, first_name, last_name, email, gender, mobile_number, date_of_birth, subjects, hobbies, picture,
                                    current_address, state, city):
        browser.all('.table').all('td').should(
            have.texts(
                ('Student Name', f'{first_name} {last_name}'),
                ('Student Email', f'{email}'),
                ('Gender', f'{gender}'),
                ('Mobile', f'{mobile_number}'),
                ('Date of Birth', f'{date_of_birth}'),
                ('Subjects', f'{subjects}'),
                ('Hobbies', f'{hobbies}'),
                ('Picture', f'{picture}'),
                ('Address', f'{current_address}'),
                ('State and City', f'{state} {city}'),
        )) """

    def fill_email(self, email):
        email_field.type(f"{email}")

    def click_gender_radiobutton(self, gender):
        gender_radiobuttons.get(f"{gender}").click()

    def fill_mobile(self, mobile):
        mobile_field.type(f"{mobile}")

    def select_subject(self, subject):
        subject_input.send_keys(f"{subject}").press_enter()

    def select_hobbies(self, hobbies):
        hobbies_checkboxes.get(f"{hobbies}").click()

    def chose_picture(self, picture_name):
        choose_picture_button.set_value(resource.path(f"{picture_name}"))

    def fill_current_address(self, current_address):
        current_address_input.type(f"{current_address}")

    def fill_state_and_city(self, state, city):
        state_input.type(f"{state}").press_enter()
        city_input.type(f"{city}").press_enter()
