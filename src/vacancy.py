class Vacancy:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, name: str, area: str, salary: int, url: str, snippet: str):
        """
        Инициализация объекта Vacancy.

        :param name: Название вакансии.
        :param area: Область (город, регион) вакансии.
        :param salary: Зарплата.
        :param url: URL вакансии.
        :param snippet: Требования к вакансии.
        """
        self.name = self.__validation_data(name)
        self.area = self.__validation_data(area)
        self.salary = salary
        self.url = url
        self.snippet = snippet

    def __str__(self):
        """
        Возвращает строковое представление объекта Vacancy.

        :return: Строка с информацией о вакансии.
        """
        return (f"{self.name}\n"
                f"Город: {self.area}\n"
                f"Зарплата: {self.salary if self.salary else 'Не указана'}\n"
                f"URL: {self.url}\n"
                f"Требования: {self.snippet}\n")

    def __lt__(self, other):
        """
        Метод для сравнения вакансий по зарплате.

        :param other: Другая вакансия для сравнения.
        :return: True, если зарплата текущей вакансии меньше зарплаты другой вакансии, иначе False.
        """
        if not self.salary:
            return 0  # "Не указана"
        elif not other.salary:
            return 0  # "Не указана"
        elif self.salary < other.salary:
            return True
        else:
            return False

    @staticmethod
    def __validation_data(data):
        """
        Метод валидации данных: если данные отсутствуют, возвращается текст "Отсутствует".

        :param data: Данные для валидации.
        :return: Валидация данных или текст "Отсутствует", если данные отсутствуют.
        """
        if data:
            return data
        else:
            return "Отсутствует"

    @classmethod
    def new_vacancy(cls, vacancy: dict):
        """
        Метод создания новой пользовательской вакансии из выгруженных с HH вакансий.

        :param vacancy: Словарь с данными вакансии, полученными из API HH.
        :return: Новый экземпляр Vacancy.
        """
        name = vacancy.get("name")
        area = vacancy.get("area").get("name")

        if vacancy.get("salary"):
            if vacancy.get("salary").get("from"):
                salary = int(vacancy.get("salary").get("from"))
            else:
                salary = 0
        else:
            salary = 0  # "Не указана"

        url = vacancy.get("url")

        if vacancy.get("snippet").get("responsibility") is not None:
            snippet = vacancy.get("snippet").get("responsibility")
        else:
            snippet = "Не указаны"

        return cls(name, area, salary, url, snippet)

