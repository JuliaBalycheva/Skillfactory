Введение
------------

Этот репозиторий содержит базовые тесты для онлайн-магазина Amazon.com.
Тесты созданы используя щаблон PageObject с Selenium и Python (PyTest + Selenium).
Создатель: Юлия Балычева

Файлы
-----

[pages/conftest.py](pages/conftest.py) содержит код для отлова падающих тестов

[pages/base.py](pages/base.py) содержит PageObject pattern для Python.

[pages/selectors.py](pages/web_element.py) содержит web elements (селекторы) на страницах

[tests/*](tests) содержит Web UI тесты для разных частей онлайн-магазина Amazon (https://amazon.com/)


Как запустить тесты
----------------

1) Установите все зависимости:

    ```bash
    pip3 install -r requirements.txt
    ```


2) Запустите тесты:

    ```bash
    python -m pytest -v --driver Chrome --driver-path Chrome/chromedriver.exe tests
    ```


Заметка:
Этот проект уже содержит Selenium Chrome Driver в папке Chrome (chromedriver.exe)
