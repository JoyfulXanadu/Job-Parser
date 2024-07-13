import sys
from src.json_worker import WorkWithJson
from src.parser import HH
from src.vacancy import Vacancy


class UserInteractive(WorkWithJson):
    """
    Класс, обеспечивающий взаимодействие с пользователем.
    Наследник класса WorkWithJson для работы с JSON файлами.
    """

    def __init__(self, user_name: str):
        """
        Инициализация объекта UserInteractive.

        :param user_name: Имя пользователя.
        """
        super().__init__()
        self.user_name = user_name
        self.vacancies_list = []

    @staticmethod
    def get_vacancies_list(keyword: str) -> list[dict]:
        """
        Получение с сайта HH списка вакансий по ключевому слову.

        :param keyword: Ключевое слово для поиска вакансий.
        :return: Список вакансий в виде словарей.
        """
        hh = HH(keyword)
        return hh.load_vacancies()

    def get_vacancies_list_from_file(self) -> list[dict]:
        """
        Получение списка вакансий из файла.

        :return: Список вакансий в виде словарей.
        """
        work_file = WorkWithJson()
        self.vacancies_list = []
        for vac in work_file.read_file():
            self.vacancies_list.append(vac)
        return self.vacancies_list

    def get_top_n_for_salary(self, n: int) -> list[dict]:
        """
        Получение заданного количества вакансий с сортировкой
        по уровню зарплат (с убыванием).

        :param n: Количество вакансий для вывода.
        :return: Список вакансий в виде словарей, отсортированный по зарплате.
        """
        vac_filter = []
        for vac in self.vacancies_list:
            vac_filter.append(vac)

        sort_by_salary = sorted(vac_filter, key=lambda x: x.salary, reverse=True)
        return sort_by_salary[:n]

    def get_vacancy_from_keywords(self) -> list[dict]:
        """
        Получение списка вакансий по заданному ключевому слову.

        :return: Список вакансий, соответствующих ключевому слову.
        """
        keywords = input("Введите ключевое слово:  ")  # Получение ключевого слова от пользователя
        print()
        res = []
        for vacancy in self.vacancies_list:
            if vacancy.name.find(keywords) != -1:
                res.append(vacancy)

        return res

    @staticmethod
    def user_interaction():
        """
        Функция для взаимодействия с пользователем.
        """

        # Приветствие и получение имени пользователя
        print("Привет")
        user_name = input("Введите своё имя:  ")
        user = UserInteractive(user_name)

        # Получение запроса для поиска вакансий и сохранение их в файл
        keyword = input("Введите запрос для поиска вакансий на HH: ")
        user.save_file(user.get_vacancies_list(keyword))

        # Удаление файла по желанию пользователя
        YesNo = input("\nФайл с вакансиями сформирован.\nУдалить файл с найденными вакансиями? "
                      "\nЕсли удаляем, то выходим из программы!\n"
                      "(Д/д, Y/y - удаляем и выходим, Н/н, N/n - продолжаем работу): ")
        if YesNo in ["Y", "y", "Д", "д"]:
            user.delete_file()
            sys.exit()

        # Получение количества вакансий для вывода и вывод топ N вакансий по зарплате
        n = int(input("\nСколько вакансий вывести на экран (введите число): "))
        print()

        # Получение списка вакансий из файла и преобразование в объекты Vacancy
        user.get_vacancies_list_from_file()
        new_vac_list = []
        for vacancy in user.vacancies_list:
            vac = Vacancy.new_vacancy(vacancy)
            new_vac_list.append(vac)

        user.vacancies_list = new_vac_list
        top_vacancies = user.get_top_n_for_salary(n)
        for vacancy in top_vacancies:
            print(vacancy)
            print()

        print("------------------------------------------------------------------")
        # Вывод вакансий по ключевому слову
        keyword_vacancies = user.get_vacancy_from_keywords()

        for vacancy in keyword_vacancies:
            print(vacancy)
            print()
