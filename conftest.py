from selene.support.shared import browser

import pytest


@pytest.fixture
def test_windows_size():
    print("preparing settings for the code executing")
    browser.config.driver = 'chrome'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield "Google Chrome"
    browser.quit()
