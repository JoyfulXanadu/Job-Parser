class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, name: str, area: str, salary: int, url: str, snippet: str):
        """
        Инициализирует объект Vacancy с атрибутами имени, города, зарплаты, ссылки и требований
        :param name: Название вакансии
        :param area: Город
        :param salary: Зарплата
        :param url: Ссылка на вакансию
        :param snippet: Краткое описание требований
        """
        self.name = self.__validation_data(name)
        self.area = self.__validation_data(area)
        self.salary = salary
        self.url = url
        self.snippet = snippet

    def __str__(self):
        """
        Форматирует объект Vacancy в строку для удобного вывода
        :return: Отформатированная строка
        """
        return (f"{self.name}\n"
                f"Город: {self.area}\n"
                f"Зарплата: {self.salary if self.salary else 'Не указана'}\n"
                f"E-mail: {self.url}\n"
                f"Требования: {self.snippet}\n")

    def __lt__(self, other):
        """
        Сравнивает текущую вакансию с другой по зарплате
        :param other: Другая вакансия
        :return: True если текущая вакансия имеет зарплату меньше, чем у другой вакансии
        """
        if not self.salary:
            return False  # "Не указана"
        elif not other.salary:
            return False  # "Не указана" у другой вакансии
        return self.salary < other.salary

    @staticmethod
    def __validation_data(data):
        """
        Метод валидации данных: если данные отстутствуют, возвращается текст "Отсутствует"
        :param data: Данные для валидации
        :return: Валидационные данные или строка "Отсутствует"
        """
        return data if data else "Отсутствует"

    @classmethod
    def new_vacancy(cls, vacancy: dict):
        """
        Метод создания новой пользовательской вакансии из выгруженных с HH вакансий
        :param vacancy: Словарь, содержащий данные о вакансии
        :return: Экземпляр класса Vacancy
        """
        name = vacancy.get("name")
        area = vacancy.get("area", {}).get("name")

        # Определение зарплаты
        salary_dict = vacancy.get("salary")
        salary = int(salary_dict.get("from")) if salary_dict and salary_dict.get("from") else 0

        url = vacancy.get("url")
        snippet = vacancy.get("snippet", {}).get("responsibility", "Не указаны")

        return cls(name, area, salary, url, snippet)
