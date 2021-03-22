# Any file used in testing should start with test_
import pytest


def test_first_program():
    print('hello')


@pytest.mark.smoke
def test_second_program():
    assert 1 == 1


def test_cross_browser(cross_browser):
    print(cross_browser)
