from selene import browser, have, command
import os


def test_fill_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('ritaTest')
    browser.element('#lastName').type('ritaTest')
    browser.element('#userEmail').type('rita@gmail.com')
    browser.element('#gender-radio-2').perform(command.js.click)
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').perform(command.js.click)
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element('[value="1998"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__month-select').element('[value="4"]').click()
    browser.element('.react-datepicker__day--005').click()
    browser.element('#subjectsInput').perform(command.js.scroll_into_view).type('comp').press_enter()
    browser.element('#hobbies-checkbox-2').perform(command.js.click)
    browser.element('#uploadPicture').send_keys(os.path.abspath('test.pic.webp'))
    browser.element('#currentAddress').type('Test Address')
    browser.element('#state').element('#react-select-3-input').type('n').press_enter()
    browser.element('#city').element('#react-select-4-input').type('d').press_enter()
    browser.element('#submit').perform(command.js.click)

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.element('.table').all('td').even.should(have.exact_texts('ritaTest ritaTest',
                                                                     'rita@gmail.com',
                                                                     'Female',
                                                                     '1234567890',
                                                                     '05 May,1998',
                                                                     'Computer Science',
                                                                     'Reading',
                                                                     'test.pic.webp',
                                                                     'Test Address',
                                                                     'NCR Delhi'))
