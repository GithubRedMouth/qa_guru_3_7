import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def set_window_size():
    browser.config.window_width = 1920
    browser.config.window_width = 1080