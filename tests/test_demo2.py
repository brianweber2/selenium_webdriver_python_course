# Any file used in testing should start with test_
import pytest


@pytest.mark.smoke
# @pytest.mark.skip
def test_first_program():
    message = 'Hello'
    assert message == 'Hi', f'Hi does not equal {message}'


# @pytest.mark.xfail
def test_second_program():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition does not match"
