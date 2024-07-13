import json
import os.path
from abc import ABC, abstractmethod

from src.parser import HH

class FileWork(ABC):
    """
    Абстрактный класс, определяющий обязательные методы для классов-потомков
    """

    def __init__(self):
        pass

    @abstractmethod
    def read_file(self):
        """
        Чтение файла
        :return: None
        """
        pass

    @abstractmethod
    def save_file(self, data):
        """
        Запись данных в файл
        :param data: Данные для записи
        :return: None
        """
        pass

    @abstractmethod
    def delete_file(self):
        """
        Удаление файла
        :return: None
        """
        pass

class WorkWithJson(FileWork):
    """
    Класс для работы с JSON файлами
    """

    def __init__(self):
        """
        Инициализирует объект с путем к файлу
        """
        self.file_name = ""
        self.abs_path = os.path.abspath("data/vacancies.json")

    def read_file(self) -> list[dict]:
        """
        Чтение данных из JSON файла
        :return: Данные, считанные из файла
        """
        with open(self.abs_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_file(self, data: list[dict]) -> None:
        """
        Запись списка данных в JSON файл
        :param data: Данные для записи
        :return: None
        """
        with open(self.abs_path, "w", encoding="utf-8") as file:
            # Запись данных в JSON файл
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_file(self) -> None:
        """
        Удаление JSON файла
        :return: None
        """
        os.remove(self.abs_path)
