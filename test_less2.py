from selene.support.shared import browser
from selene import be, have
from conftest import testwindowsize
import pytest



def test_browser_open(testwindowsize):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_emptysearch(testwindowsize):
    browser.open('https://google.com')
    query = "sdjkfhsdflkjsdhflksdjfhsdlkjfhsdlkfjhsdlfkjshdflkjsdhflksdjfhsdlkf"
    browser.element('[name="q"]').should(be.blank).type(query).press_enter()
    browser.element('#extabar').should(have.text('כ-0 תוצאות')) #describe that found 0 results




