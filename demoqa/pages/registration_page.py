import calendar
from enum import Enum
from typing import List

from selene import browser, have, command

from demoqa import resource


class Hobbies(Enum):
    SPORTS = "Sports"
    READING = "Reading"
    MUSIC = "Music"


class RegistrationPage:
    def __init__(self):
        self.FORM_PAGE_URL = "/automation-practice-form"
        self.first_name_field = browser.element("#firstName")
        self.last_name_field = browser.element("#lastName")
        self.email_field = browser.element("#userEmail")
        self.mobile_field = browser.element("#userNumber")
        self.date_of_birth_field = browser.element("#dateOfBirthInput")
        self.subject_input = browser.element("#subjectsInput")
        self.current_address_input = browser.element("#currentAddress")
        self.choose_picture_button = browser.element("#uploadPicture")
        self.state_input = browser.element("#react-select-3-input")
        self.city_input = browser.element("#react-select-4-input")
        self.state_dropdown_elements = browser.all(
            '[id ^= "react-select"][id *= "option"]'
        )
        self.city_dropdown_elements = browser.all(
            '[id ^= "react-select"][id *= "option"]'
        )
        self.submit_button = browser.element("#submit")
        self.gender_radiobuttons = {
            "Male": browser.element('[for = "gender-radio-1"]'),
            "Female": browser.element('[for = "gender-radio-2"]'),
            "Other": browser.element('[for = "gender-radio-3"]'),
        }
        self.gender_radiobuttons_2 = {
            "Male": browser.all('[for ^= "gender-radio"]').element_by(
                have.text("Male")
            ),
            "Female": browser.all('[for ^= "gender-radio"]').element_by(
                have.text("Female")
            ),
            "Other": browser.all('[for ^= "gender-radio"]').element_by(
                have.text("Other")
            ),
        }
        self.datepicker = {
            "month_dropdown": browser.element(".react-datepicker__month-select"),
            "year_dropdown": browser.element(".react-datepicker__year-select"),
            "days": browser.element(".react-datepicker__month"),
        }
        self.hobbies_locator = browser.all('[for ^= "hobbies-checkbox"]')
        self.confirmation_popup_title_element = browser.element(
            "#example-modal-sizes-title-lg"
        )
        self.registered_user_data = browser.all(".table").all("td")

    def open(self):
        browser.open(self.FORM_PAGE_URL)
        return self

    def fill_first_name(self, value):
        self.first_name_field.type(f"{value}")
        return self

    def fill_last_name(self, last_name):
        self.last_name_field.type(f"{last_name}")
        return self

    def fill_date_of_birth(self, date_of_birth):
        self.date_of_birth_field.click()
        month_name = calendar.month_name[date_of_birth.month]

        self.datepicker.get("year_dropdown").send_keys(str(date_of_birth.year))
        self.datepicker.get("month_dropdown").send_keys(month_name)
        day = f"{date_of_birth.day:02}"
        browser.element(f".react-datepicker__day--0{day}").click()
        return self

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
        self.email_field.type(f"{email}")
        return self

    def click_gender_radiobutton(self, gender):
        self.gender_radiobuttons.get(f"{gender}").click()
        return self

    def fill_mobile(self, mobile):
        self.mobile_field.type(f"{mobile}")
        return self

    def select_subject(self, subject: List[str]):
        for i in subject:
            self.subject_input.send_keys(f"{i}").press_enter()
        return self

    def select_hobby(self, hobby: Hobbies):
        self.hobbies_locator.element_by(have.text(hobby.value)).click()
        return self

    def chose_picture(self, picture_name):
        self.choose_picture_button.set_value(resource.path(f"{picture_name}"))
        return self

    def fill_current_address(self, current_address):
        self.current_address_input.type(f"{current_address}")
        return self

    def fill_state_and_city(self, state, city):
        self.state_input.type(f"{state}").press_enter()
        self.city_input.type(f"{city}").press_enter()
        return self

    def click_submit_button(self):
        browser.element("#submit").perform(command.js.click)

    def should_registered_user_with(
        self,
        full_name,
        email,
        gender,
        mobile,
        date_of_birth,
        subjects,
        hobbies,
        picture,
        address,
        state_and_city,
    ):
        browser.element(".table").all("td").even.should(
            have.texts(
                full_name,
                email,
                gender,
                mobile,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                address,
                state_and_city,
            )
        )

    def should_confirmation_popup_title(self, title):
        self.confirmation_popup_title_element.should(have.exact_text(title))
