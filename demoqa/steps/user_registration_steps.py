from selene import browser, have

from demoqa.pages.registration_page import RegistrationPage

confirmation_popup_title_element = browser.element("#example-modal-sizes-title-lg")

class UserRegistrationSteps:
    def __init__(self):
        self.page = RegistrationPage()

    def open(self):
        self.page.open()
        return self

    def register(self):
        (
        self.page
         .fill_first_name("Kurva")
         .fill_last_name("Bobr")
         .fill_email("kurvabobr@gmail.com")
         .click_gender_radiobutton('Male')
         .fill_mobile("1234567890")
         .fill_date_of_birth("2022", "April", "19")
         .select_subject("Com")
         .select_hobbies("Music")
         .chose_picture("robert.webp")
         .fill_current_address("202-2 Dunsheath Way")
         .fill_state_and_city("NCR", "Noida")
         .click_submit_button()
         )
        return self

    def should_be_displayed_user_registered_data(
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
        browser.element(".table").all("td").should(
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
        return self

    def should_confirmation_popup_title(self, title):
        confirmation_popup_title_element.should(have.exact_text(title))
        return self


