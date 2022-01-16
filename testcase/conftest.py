import pytest


@pytest.fixture(scope='function', params=['jiajia', 'dingding'])
def my_fixture(request):
    print("这是前置")
    yield request.param
    print("这是后置")