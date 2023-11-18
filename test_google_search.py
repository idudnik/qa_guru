from selene.support.shared import browser
from selene import be, have
from conftest import test_windows_size


def test_browser_open(test_windows_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_empty_search(test_windows_size):
    browser.open('https://google.com')
    query = "sdjkfhsdflkjsdhflksdjfhsdlkjfhsdlkfjhsdlfkjshdflkjsdhflksdjfhsdlkf"
    browser.element('[name="q"]').should(be.blank).type(query).press_enter()
    browser.element('#extabar').should(have.text('כ-0 תוצאות'))  # describe that found 0 results
