Данная программа представляет собой способ взаимодействия с сайтом поиска работы hh.ru Позволяет выбрать вакансии по названию, критериям сортирует вакансии Выводит отсортированные данные в колличестве, запрошенные пользователем


Структура проекта Job-Parser
Job-Parser/
├── data
│   ├── __init__.py
│   ├── vacancies.json
├── src
│   ├── __init__.py
│   ├── custom_functionality.py
│   ├── json_worker.py
│   ├── parser.py
│   ├── vacancy.py
├── tests
│   ├── __init__.py
│   ├── tests_functionality.py
├── .gitignore
├── main.py
├── README.md

## Запуск проекта

1. Клонировать репозиторий:
    ```sh
    git clone https://github.com/JoyfulXanadu/Job-Parser.git
    ```
2. Перейти в папку проекта:

    ```sh
    cd Job-Parser
    ```

3. Создать виртуальное окружение и активировать его:
    ```sh
    python -m venv venv
    source venv/bin/activate   # Для Windows используйте `venv\Scripts\activate`
    ```

4. Установить необходимые зависимости :
    ```sh
    pip install requests
    ```

5. Запустить проект:

    ```sh
    python -m Job-Parser.main
    ```

# Как использовать
Зайти в папку Job-Parser и запустить файл main.py

После запуска в консоле будут выводится вопросы отвечаем на них и получаем вакансии





