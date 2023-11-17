from selene.support.shared import browser
from selene import be, have

import pytest
@pytest.fixture
def testwindowsize():
    print("preparing settings for the code executing")

    browser.config.window_width = 1690
    browser.config.window_height = 1080

    yield
    browser.quit()
    # print("success")
