import pytest


@pytest.fixture(scope='class')
def setup():
    print('I will be executed first.')
    yield
    print('I will be executed last for teardown methods.')


@pytest.fixture()
def load_data():
    print('User profile data is being created.')
    return ['Brian', 'Weber', 'www.brianwweber.com']


@pytest.fixture(params=['Chrome', 'Firefox', 'IE'])
def cross_browser(request):
    return request.param
