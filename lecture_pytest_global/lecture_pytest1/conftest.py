import pytest



@pytest.fixture(autouse=True)
def test_fixture_1():
    print("global lecture_pytest_fixture_1 fixture setup")
    yield
    print("global lecture_pytest_fixture_1 fixture teardown")


@pytest.fixture(autouse=False)
def test_fixture_2():
    print("return type of 5 fixture")
    return 5
