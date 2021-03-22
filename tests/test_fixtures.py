import pytest


@pytest.mark.usefixtures('setup')
class TestExample:

    def test_fixture_demo(self):
        print('I will execute steps in test_fixture_demo.')

    def test_fixture_demo2(self):
        print('I will execute steps in test_fixture_demo.')

    def test_fixture_demo3(self):
        print('I will execute steps in test_fixture_demo.')
