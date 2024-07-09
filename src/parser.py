from abc import ABC, abstractmethod
import requests


class Parser(ABC):
    """
    Абстрактный класс Parser, который определяет метод для загрузки вакансий.
    """

    @abstractmethod
    def load_vacancies(self):
        """
        Загружает вакансии.

        :return: Список вакансий.
        """
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter (HH).

    """

    def init(self, keyword: str):
        """
        Инициализация класса HH.

        :param keyword: Ключевое слово для поиска вакансий.
        """
        self.url = 'https://api.hh.ru/vacancies'  # URL API для вакансий HeadHunter
        self.headers = {'User-Agent': 'HH-User-Agent'}  # Заголовки для запроса
        self.params = {'text': keyword, 'page': 0, 'per_page': 100}  # Параметры запроса

    def load_vacancies(self) -> list[dict]:
        """
        Загружает вакансии с HeadHunter API.

        :return: Список вакансий (словарей).
        """
        vacancies = []  # Список для сохранения вакансий

        # Запросы продолжаются пока не будет достигнута 20-я страница результатов
        while self.params.get('page') != 20:
            # Выполнение GET-запроса к API
            response = requests.get(self.url, headers=self.headers, params=self.params)

            # Проверка успешности запроса
            if response.status_code == 200:
                # Парсинг JSON-ответа и добавление вакансий в список
                items = response.json()['items']
                vacancies.extend(items)

                # Переход на следующую страницу результатов
                self.params['page'] += 1
            else:
                break  # Прерывание цикла в случае ошибки запроса

        return vacancies
