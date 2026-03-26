from enum import Enum
from typing import List

import allure
from selene import browser, have, command

from demoqa import resource


class Hobby(Enum):
    SPORTS = "Sports"
    READING = "Reading"
    MUSIC = "Music"


class Subject(Enum):
    COMPUTER_SCIENCE = "Computer Science"
    ENGLISH = "English"
    ARTS = "Arts"
    ECONOMICS = "Economics"


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


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
        with allure.step("Filling first name"):
            self.first_name_field.type(f"{value}")
            return self

    def fill_last_name(self, last_name):
        with allure.step("Filling last name"):
            self.last_name_field.type(f"{last_name}")
            return self

    def fill_date_of_birth(self, date_of_birth):
        with allure.step("Filling date of birth"):
            self.date_of_birth_field.click()

            self.datepicker.get("year_dropdown").send_keys(date_of_birth.strftime("%Y"))
            self.datepicker.get("month_dropdown").send_keys(
                date_of_birth.strftime("%B")
            )
            day = f"{date_of_birth.day:02}"
            browser.element(f".react-datepicker__day--0{day}").click()
        return self

    def fill_email(self, email):
        with allure.step("Filling email"):
            self.email_field.type(f"{email}")
        return self

    def click_gender_radiobutton(self, gender: Gender):
        with allure.step(f"Selecting gender {gender.value}"):
            self.gender_radiobuttons.get(gender.value).click()
        return self

    def fill_mobile(self, mobile):
        with allure.step("Filling mobile number"):
            self.mobile_field.type(f"{mobile}")
        return self

    def select_subject(self, subject: List[Subject]):
        with allure.step(f"Selecting subject"):
            for i in subject:
                self.subject_input.send_keys(f"{i.value}").press_enter()
        return self

    def select_hobby(self, hobby: List[Hobby]):
        with allure.step(f"Selecting hobby"):
            for i in hobby:
                self.hobbies_locator.element_by(have.text(i.value)).click()
        return self

    def chose_picture(self, picture_name):
        with allure.step(f"Selecting picture: {picture_name}"):
            self.choose_picture_button.set_value(resource.path(f"{picture_name}"))
        return self

    def fill_current_address(self, current_address):
        with allure.step(f"Filling current address"):
            self.current_address_input.type(f"{current_address}")
        return self

    def fill_state_and_city(self, state, city):
        with allure.step(f"Selecting state and city"):
            self.state_input.type(f"{state}").press_enter()
            self.city_input.type(f"{city}").press_enter()
        return self

    def click_submit_button(self):
        with allure.step(f"Clicking submit button"):
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
        with allure.step(
            f"Checking that entered user data displayed correctly in the summary table"
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
        with allure.step("Checking title of popup"):
            self.confirmation_popup_title_element.should(have.exact_text(title))
