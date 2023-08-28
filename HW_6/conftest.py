import pytest



@pytest.fixture(autouse=False)
def fixture_global():
    print("global HW_6 fixture setup")
    yield
    print("global HW_6 fixture teardown")
