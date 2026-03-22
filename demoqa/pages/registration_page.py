from selene import browser, have, command

from demoqa import resource

FORM_PAGE_URL = "/automation-practice-form"
# GIVEN
first_name_field = browser.element("#firstName")
last_name_field = browser.element("#lastName")
email_field = browser.element("#userEmail")
mobile_field = browser.element("#userNumber")
date_of_birth_field = browser.element("#dateOfBirthInput")

subject_input = browser.element("#subjectsInput")
current_address_input = browser.element("#currentAddress")
choose_picture_button = browser.element("#uploadPicture")
state_input = browser.element("#react-select-3-input")
city_input = browser.element("#react-select-4-input")
state_dropdown_elements = browser.all('[id ^= "react-select"][id *= "option"]')
city_dropdown_elements = browser.all('[id ^= "react-select"][id *= "option"]')

submit_button = browser.element("#submit")

gender_radiobuttons = {
    "Male": browser.element('[for = "gender-radio-1"]'),
    "Female": browser.element('[for = "gender-radio-2"]'),
    "Other": browser.element('[for = "gender-radio-3"]'),
}
gender_radiobuttons_2 = {
    "Male": browser.all('[for ^= "gender-radio"]').element_by(have.text("Male")),
    "Female": browser.all('[for ^= "gender-radio"]').element_by(have.text("Female")),
    "Other": browser.all('[for ^= "gender-radio"]').element_by(have.text("Other")),
}
datepicker = {
    "month_dropdown": browser.element(".react-datepicker__month-select"),
    "year_dropdown": browser.element(".react-datepicker__year-select"),
    "days": browser.element(".react-datepicker__month"),
}

hobbies_checkboxes = {
    "Sports": browser.all('[for ^= "hobbies-checkbox"]').element_by(
        have.text("Sports")
    ),
    "Reading": browser.all('[for ^= "hobbies-checkbox"]').element_by(
        have.text("Reading")
    ),
    "Music": browser.all('[for ^= "hobbies-checkbox"]').element_by(have.text("Music")),
}

confirmation_popup_title_element = browser.element("#example-modal-sizes-title-lg")


class RegistrationPage:
    def __init__(self):
        self.registered_user_data = browser.all(".table").all("td")

    def open(self):
        browser.open(FORM_PAGE_URL)
        return self

    def fill_first_name(self, value):
        first_name_field.type(f"{value}")
        return self

    def fill_last_name(self, last_name):
        last_name_field.type(f"{last_name}")
        return self

    def fill_date_of_birth(self, year, month, day):
        date_of_birth_field.click()
        datepicker.get("year_dropdown").send_keys(year)
        datepicker.get("month_dropdown").send_keys(month)
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
        email_field.type(f"{email}")
        return self

    def click_gender_radiobutton(self, gender):
        gender_radiobuttons.get(f"{gender}").click()
        return self

    def fill_mobile(self, mobile):
        mobile_field.type(f"{mobile}")
        return self

    def select_subject(self, subject):
        subject_input.send_keys(f"{subject}").press_enter()
        return self

    def select_hobbies(self, hobbies):
        hobbies_checkboxes.get(f"{hobbies}").click()
        return self

    def chose_picture(self, picture_name):
        choose_picture_button.set_value(resource.path(f"{picture_name}"))
        return self

    def fill_current_address(self, current_address):
        current_address_input.type(f"{current_address}")
        return self

    def fill_state_and_city(self, state, city):
        state_input.type(f"{state}").press_enter()
        city_input.type(f"{city}").press_enter()
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
        confirmation_popup_title_element.should(have.exact_text(title))
