from abc import ABC, abstractmethod
import requests


class Parser(ABC):
    """
    Класс Parser является родительским классом, который необходимо реализовать.
    Все парсеры должны наследовать этот класс и реализовывать его методы.
    """

    @abstractmethod
    def load_vacancies(self):
        """
        Абстрактный метод для загрузки вакансий.
        Необходимо реализовать в каждом классе-наследнике.
        """
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter.
    """

    def __init__(self, keyword: str):
        """
        Инициализация объекта HH.

        :param keyword: Ключевое слово для поиска вакансий.
        """
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': keyword, 'page': 0, 'per_page': 100}

    def load_vacancies(self) -> list[dict]:
        """
        Загрузка вакансий с HeadHunter API.

        :return: Список словарей с информацией о вакансиях.
        """
        vacancies = []

        # Цикл для перебора страниц с вакансиями.
        while self.params.get('page') != 20:
            # Отправка GET-запроса к API
            response = requests.get(self.url, headers=self.headers, params=self.params)
            # Парсинг ответа в формат JSON и добавление вакансий в список
            vacancies.extend(response.json().get('items', []))
            # Переход на следующую страницу
            self.params['page'] += 1

        return vacancies
