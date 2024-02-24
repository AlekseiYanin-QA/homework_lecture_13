from selene import browser, have
from pages.registration_page import RegistrationPage


def test_positive_form_registration():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Alex')
    registration_page.fill_last_name('Yanin')
    registration_page.fill_email('test@test.ru')
    registration_page.select_gender("Male")
    registration_page.fill_phone_number('7916896581')
    registration_page.fill_date_of_birth("1982", "April", "10")
    registration_page.type_subjects('Computer Science')
    registration_page.select_hobbies()
    registration_page.upload_picture('photo.jpg')
    registration_page.type_current_address('random residential address')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Delhi')
    registration_page.submit()

    # THEN
    browser.element('.table').all('td').even.should(
        have.texts('Alex Yanin',
                   'test@test.ru',
                   'Male',
                   '7916896581',
                   '10 April,1982',
                   'Computer Science',
                   'Sports, Reading, Music',
                   'photo.jpg',
                   'random residential address',
                   'NCR Delhi'))
