import sys

from src.json_worker import WorkWithJson
from src.parser import HH
from src.vacancy import Vacancy


class UserInteractive(WorkWithJson):
    """
    Класс, обеспечивающий взаимодействие с пользователем.
    Наследуется от WorkWithJson.
    """

    def init(self, user_name: str):
        """
        Инициализация класса.

        :param user_name: Имя пользователя.
        """
        super().init()  # Вызов инициализации родительского класса.
        self.user_name = user_name  # Сохранение имени пользователя.
        self.vacancies_list = []  # Инициализация списка вакансий.

    @staticmethod
    def get_vacancies_list(keyword: str):
        """
        Получение с сайта HH списка вакансий по ключевому слову.

        :param keyword: Ключевое слово для поиска вакансий.
        :return: Список вакансий.
        """
        hh = HH(keyword)
        return hh.load_vacancies()

    def get_vacancies_list_from_file(self) -> list[dict]:
        """
        Чтение списка вакансий из файла.

        :return: Список вакансий.
        """
        work_file = WorkWithJson()
        self.vacancies_list = []  # Очистка текущего списка вакансий.
        for vac in work_file.read_file():
            self.vacancies_list.append(vac)
        return self.vacancies_list

    def get_top_n_for_salary(self, n: int) -> list[dict]:
        """
        Получение топ N вакансий с самой высокой зарплатой.

        :param n: Количество вакансий для отображения.
        :return: Список топ N вакансий по уровню зарплаты.
        """
        vac_filter = []
        for vac in self.vacancies_list:
            vac_filter.append(vac)

        # Сортировка вакансий по зарплате (убывание).
        sort_by_salary = sorted(vac_filter, key=lambda x: x.salary, reverse=True)
        return sort_by_salary[:n]

    def get_vacancy_from_keywords(self) -> list[dict]:
        """
        Поиск вакансий по ключевому слову, введенному пользователем.

        :return: Список вакансий, соответствующих ключевому слову.
        """
        keywords = input("Введите ключевое слово:  ")
        print()
        res = []
        for vacancy in self.vacancies_list:
            if vacancy.name.find(keywords) != -1:
                res.append(vacancy)

        return res

    @staticmethod
    def user_interaction(self):
        """
        Функция для взаимодействия с пользователем.

        Включает запросы к пользователю о его имени, ключевом слове для
        поиска вакансий и дальнейшие действия.

        :param self: Ссылка на текущий объект класса.
        :return: None
        """
        print("Привет")
        user_name = input("Как ваше имя?  ")
        user = UserInteractive(user_name)

        keyword = input("Введите запрос (ключевое слово для поиска вакансий на HH): ")

        # Сохранение списка вакансий в файл.
        user.save_file(user.get_vacancies_list(keyword))

        YesNo = input("\nФайл с вакансиями сформирован.\nУдалить файл с найденными вакансиями? "
                      "\nЗа удалением файла следует выход из программы!!!\n"
                      "(Д/д, Y/y - удаляем и выходим, Н/н, N/n - продолжаем работу): ")
        if YesNo == "Y" or YesNo == "y" or YesNo == "Д" or YesNo == "д":
            user.delete_file()
            sys.exit()

        n = int(input("\nКакое количество вакансий вывести?:  "))
        print()

        user.get_vacancies_list_from_file()  # Чтение вакансий из файла.

        # Преобразование вакансий в объекты Vacancy.
        new_vac_list = []
        for vacancy in user.vacancies_list:
            vac = Vacancy.new_vacancy(vacancy)
            new_vac_list.append(vac)

        user.vacancies_list = new_vac_list

        # Вывод топ N вакансий по зарплате.
        user.get_top_n_for_salary(n)
        for vacancy in user.get_top_n_for_salary(n):
            print(vacancy)
            print()

        print("------------------------------------------------------------------")

        # Вывод вакансий, найденных по ключевому слову.
        for vacancy in user.get_vacancy_from_keywords():
            print(vacancy)
            print()
