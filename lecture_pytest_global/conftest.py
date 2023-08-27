import pytest



@pytest.fixture(autouse=False)
def fixture_global():
    print("global lecture_pytest_global fixture setup")
    yield
    print("global lecture_pytest_global fixture teardown")
