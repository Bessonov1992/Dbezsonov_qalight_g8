def test_1():
    print("lecture_pytest_test_1 test executed")


def test_2(test_fixture_global):
    print("lecture_pytest_test_2 test executed")


def test_3(test_fixture_global,test_fixture_2):
    print(type(test_fixture_2))