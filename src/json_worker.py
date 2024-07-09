from abc import ABC, abstractmethod
import os
import json

class FileWork(ABC):
    """
    Абстрактный класс, определяющий обязательные методы для классов-потомков.
    """

    def init(self):
        """
        Инициализация класса (может быть переопределена в классах-потомках).
        """
        pass

    @abstractmethod
    def read_file(self):
        """
        Чтение файла.

        :return: None
        """
        pass

    @abstractmethod
    def save_file(self, data):
        """
        Запись в файл.

        :param data: Данные для записи в файл.
        :return: None
        """
        pass

    @abstractmethod
    def delete_file(self):
        """
        Удаление файла.

        :return: None
        """
        pass


class WorkWithJson(FileWork):
    """
    Класс для работы с JSON файлами.
    Наследуется от абстрактного класса FileWork и реализует его методы.
    """

    def init(self):
        """
        Инициализация класса. Устанавливает имя файла и абсолютный путь к нему.
        """
        self.file_name = "vacancies.json"
        self.abs_path = os.path.abspath(f"data/{self.file_name}")

    def read_file(self) -> list:
        """
        Чтение данных из JSON файла.

        :return: Данные, считанные из файла (список словарей).
        """
        with open(self.abs_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_file(self, data: list[dict]) -> None:
        """
        Запись данных в JSON файл.

        :param data: Данные для записи в файл (список словарей).
        :return: None
        """
        with open(self.abs_path, "w", encoding="utf-8") as file:
            # Запись данных в файл с форматированием.
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_file(self) -> None:
        """
        Удаление JSON файла.

        :return: None
        """
        return os.remove(self.abs_path)
