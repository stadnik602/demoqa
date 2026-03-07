from selene import browser, have, command

from demoqa.pages.registration_page import (
    RegistrationPage,
    confirmation_popup_title_element,
)

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
    registration_page.should_confirmation_popup_title("Thanks for submitting the form")
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


"""    registration_page.should_registered_user_with(
        "Kurva Bobr",
        "kurvabobr@gmail.com",
        "Male",
        "1234567890",
        "19 April,2022",
        "Computer Science",
        "Music",
        "robert.webp",
        "202-2 Dunsheath Way",
        "NCR Noida",
    )"""


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
