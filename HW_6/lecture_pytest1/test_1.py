def test_1():
    print("lecture_pytest_test_1 test executed")


def test_2(fixture_global):
    print("lecture_pytest_test_2 test executed")


def test_3(fixture_global, fixture_2):
    print(type(fixture_2))
