import pytest



@pytest.fixture(autouse=True)
def fixture_1():
    print("global lecture_pytest_fixture_1 fixture setup")
    yield
    print("global lecture_pytest_fixture_1 fixture teardown")


@pytest.fixture(autouse=False)
def fixture_2():
    print("return type of 5 fixture")
    yield 5
