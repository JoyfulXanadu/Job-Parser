import pytest
from src.custom_functionality import UserInteractive
from src.vacancy import Vacancy


@pytest.fixture()
def test():
    """
    Текстура формирует 10 экземпляров тестовых вакансий
    :return:
    """
    test = UserInteractive("name")
    # test_list = [Vacancy(name=f"testname {i}", area=f"testarea {i}", salary=i * 1000, url=f"testurl {i}", snippet=f"testsnippet {i}") for i in range(10)]
    test_list = []
    for i in range(10):
        vac = Vacancy(
            name=f"testname {i}",
            area=f"testarea {i}",
            salary=i * 1000,
            url=f"testurl {i}",
            snippet=f"testsnippet {i}")
        test_list.append(vac)
    test.vacancies_list = test_list
    return test


def test_get_top_n_for_salary(test):
    """
    Тестирование варианта, когда на вход метода подается пустой список
    :param test:
    :return:
    """
    assert UserInteractive.get_top_n_for_salary(test, 0) == []


def test_get_top_n_for_salary_2(test):
    """
    Тестирование варианта, когда на вход метода подаются 5 вакансий
    :param test:
    :return:
    """
    assert len(UserInteractive.get_top_n_for_salary(test, 5)) == 5


def test_get_top_n_for_salary_3(test):
    """
    Тестирование зарплаты в последней тестовой вакансии
    :param test:
    :return:
    """
    assert UserInteractive.get_top_n_for_salary(test, 1)[0].salary == 9000