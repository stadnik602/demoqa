from selene import browser, have, command

from demoqa.pages.registration_page import RegistrationPage

"""    def registered_user_data(self):
        browser.all('.table').all('td').should(
            have.texts(
                ('Student Name', 'Kurva Bobr'),
                ('Student Email', 'kurvabobr@gmail.com'),
                ('Gender', 'Male'),
                ('Mobile', '1234567890'),
                ('Date of Birth', '19 April,2022'),
                ('Subjects', 'Computer Science'),
                ('Hobbies', 'Music'),
                ('Picture', 'robert.webp'),
                ('Address', '202-2 Dunsheath Way'),
                ('State and City', 'NCR Noida'),
            ))"""


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

confirmation_popup_title_element = "#example-modal-sizes-title-lg"


def test_successes_submit_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name("Kurva")
    registration_page.fill_last_name("Bobr")
    registration_page.fill_email("kurvabobr@gmail.com")
    registration_page.click_gender_radiobutton("Male")
    registration_page.fill_mobile("1234567890")
    registration_page.fill_date_of_birth("2022", "April", "19")
    registration_page.select_subject("Com")
    registration_page.select_hobbies("Music")
    registration_page.chose_picture("robert.webp")
    registration_page.fill_current_address("202-2 Dunsheath Way")
    registration_page.fill_state_and_city("NCR", "Noida")
    """    current_address_input.with_(set_value_by_js=True).set_value('202-2 Dunsheath Way')
    current_address_input.perform(command.js.set_value('202-2 Dunsheath Way'))"""

    browser.element("#submit").perform(command.js.click)

    # THEN
    """registration_page.should_registered_user_with(
        'Kurva',
        'Bobr',
        'kurvabobr@gmail.com',
        'Male',
        '1234567890',
        '19 April,2022',
        'Computer Science',
        'Music',
        'robert.webp',
        '202-2 Dunsheath Way',
        'NCR',
        'Noida'
            )"""
    registration_page.registered_user_data.should(
        have.exact_texts(
            ("Student Name", "Kurva Bobr"),
            ("Student Email", "kurvabobr@gmail.com"),
            ("Gender", "Male"),
            ("Mobile", "1234567890"),
            ("Date of Birth", "19 April,2022"),
            ("Subjects", "Computer Science"),
            ("Hobbies", "Music"),
            ("Picture", "robert.webp"),
            ("Address", "202-2 Dunsheath Way"),
            ("State and City", "NCR Noida"),
        )
    )

    browser.element(confirmation_popup_title_element).should(
        have.exact_text("Thanks for submitting the form")
    )
    """browser.element('.table').all('td').even.should(
        have.texts(
            'Kurva Bobr',
            'kurvabobr@gmail.com',
            'Male',
            '1234567890',
            '19 April,2022',
            'Computer Science',
            'Music',
            'robert.webp',
            '202-2 Dunsheath Way',
            'NCR Noida',
        ))"""


"""    browser.all('.table td:nth-child(2)').should(
        have.texts(
            'Kurva Bobr',
            'kurvabobr@gmail.com',
            'Male',
            '1234567890',
            '19 April,2022',
            'Computer Science',
            'Music',
            'robert.webp',
            '202-2 Dunsheath Way',
            'NCR Noida'
        )
    )"""
