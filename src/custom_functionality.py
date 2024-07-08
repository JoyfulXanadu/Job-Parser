import sys
from src.json_worker import WorkWithJson
from src.parser import HH
from src.vacancy import Vacancy


class UserInteractive:
    pass


class UserInteractive(WorkWithJson):
    """
    Класс, обеспечивающий взаимодействие с пользователем
    """

    def __init__(self, user_name: str):
        """
        Инициализация пользователя и списка вакансий
        :param user_name: Имя пользователя
        """
        super().__init__()  # Корректная инициализация базового класса
        self.user_name = user_name
        self.vacancies_list = []

    @staticmethod
    def get_vacancies_list(keyword: str):
        """
        Получение с сайта HH списка вакансий по ключевому слову
        :param keyword: Ключевое слово для поиска вакансий
        :return: Список вакансий
        """
        hh = HH(keyword)
        return hh.load_vacancies()

    def get_vacancies_list_from_file(self) -> list[dict]:
        """
        Получение списка вакансий из файла
        :return: Список вакансий
        """
        self.vacancies_list = []
        for vac in self.read_file():  # Чтение из файла JSON для текущего экземпляра
            self.vacancies_list.append(vac)
        return self.vacancies_list

    def get_top_n_for_salary(self, n: int) -> list[dict]:
        """
        Получение топ N вакансий по уровню зарплат, отсортированных по убыванию.
        :param n: Количество вакансий для вывода
        :return: Список топ N вакансий
        """
        sorted_vacancies = sorted(self.vacancies_list, key=lambda x: x['salary'], reverse=True)
        return sorted_vacancies[:n]

    def get_vacancy_from_keywords(self) -> list[dict]:
        """
        Получение списка вакансий по ключевому слову, введенному пользователем.
        :return: Список вакансий, удовлетворяющих ключевому слову
        """
        keywords = input("Пожалуйста, введите ключевое слово для поиска вакансий: ")
        print()
        res = []
        for vacancy in self.vacancies_list:
            if vacancy['name'].find(keywords) != -1:
                res.append(vacancy)
        return res

    def user_interaction(self):
        """
        Функция для взаимодействия с пользователем.
        :return: None
        """
        # Приветствие пользователя
        print("Здравствуйте, пользователь!")
        user_name = input("Как вы предпочитаете, чтобы вас называли? ")
        self.user_name = user_name

        # Запрос ключевого слова для поиска вакансий
        keyword = input("Пожалуйста, введите ключевое слово для поиска вакансий на HH: ")

        # Сохранение полученного списка вакансий в файл
        self.save_file(self.get_vacancies_list(keyword))

        # Опция удаления файла с вакансиями
        YesNo = input("\nСписок вакансий сохранен.\nХотите ли вы удалить файл с найденными вакансиями? "
                      "\n(Д/д, Y/y - удалить и выйти, Н/н, N/n - продолжить работу): ")
        if YesNo in ["Y", "y", "Д", "д"]:
            self.delete_file()
            sys.exit()

        # Запрос количества вакансий для вывода на экран
        n = int(input("\nСколько вакансий вы хотите увидеть на экране? Пожалуйста, введите число: "))
        print()

        # Получение списка вакансий из файла и вывод топ N вакансий по зарплате
        self.get_vacancies_list_from_file()

        new_vac_list = []
        for vacancy in self.vacancies_list:
            vac = Vacancy.new_vacancy(vacancy)
            new_vac_list.append(vac)

        self.vacancies_list = new_vac_list
        top_vacancies = self.get_top_n_for_salary(n)
        for vacancy in top_vacancies:
            print(vacancy)
            print()

        print("------------------------------------------------------------------")

        # Получение списка вакансий по ключевому слову и их вывод на экран
        keyword_vacancies = self.get_vacancy_from_keywords()
        for vacancy in keyword_vacancies:
            print(vacancy)
            print()

    if __name__ == "__main__":
        user_interface = UserInteractive("")
        user_interface.user_interaction()

