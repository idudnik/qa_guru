from selene.support.shared import browser
from selene import be, have
import time
import pytest

@pytest.fixture
def test_windowsize():
    print("preparing settings for the code executing")

    browser.config.driver.set_window_size(1690, 1080)

    yield
    browser.quit()
    print("success")


def test_browser_open(test_windowsize):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_emptysearch(test_windowsize):
    browser.open('https://google.com')
    query = "sdjkfhsdflkjsdhflksdjfhsdlkjfhsdlkfjhsdlfkjshdflkjsdhflksdjfhsdlkf"
    browser.element('[name="q"]').should(be.blank).type(query).press_enter()
    browser.element('#extabar').should(have.text('כ-0 תוצאות')) #describe that found 0 results




