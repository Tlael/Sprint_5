# Sprint 5 — UI автотесты на Python (Selenium + Pytest)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![tests](https://img.shields.io/badge/tests-pytest-green)
![selenium](https://img.shields.io/badge/selenium-WebDriver-brightgreen)
![status](https://img.shields.io/badge/status-active-success)

Учебный проект по автоматизации UI-тестирования сервиса Stellar Burgers.  
Тесты написаны на **Python** с использованием **Selenium WebDriver** и **pytest**.

---

## Функциональность

Покрыты основные пользовательские сценарии:

- регистрация нового пользователя;
- логин по разным точкам входа;
- логаут из личного кабинета;
- переход между конструктором и личным кабинетом;
- переход из личного кабинета в конструктор через логотип и кнопку «Конструктор».

---

## Стек

- Python 3.x  
- Selenium WebDriver  
- pytest  
- webdriver-manager  

---

## Структура проекта

```text
Sprint_5/
│
├── tests/                         # Тесты (pytest)
│   ├── conftest.py                # Фикстуры, драйвер, хелперы
│   ├── test_account_go_to_constructor.py
│   ├── test_constructor_burger.py
│   ├── test_go_to_account.py
│   ├── test_login.py
│   ├── test_logout.py
│   └── test_registration.py
│
├── locators/                      # Локаторы страниц
│   └── locators.py                # (название укажи, как в проекте)
│
├── data.py                        # Тестовые данные (логины, пароли и т.п.)
├── urls.py                        # Базовый URL и адреса страниц
│
├── pytest.ini                     # Конфигурация pytest
├── requirements.txt               # Зависимости проекта
├── .gitignore                     # Игнорируемые файлы/папки
└── README.md                      # Описание проекта
   ``` 

Как запустить

1. Клонировать репозиторий
   ```bash
    git clone https://github.com/Tlael/Sprint_5.git
    cd Sprint_5
   ```

2. Создать и активировать виртуальное окружение (по желанию)
   ```bash
    python -m venv venv
    source venv/bin/activate      # Linux / macOS
    # или
    venv\Scripts\activate         # Windows
   ```

3. Установить зависимости
   ```bash
    pip install -r requirements.txt
   ```

4. Запустить тесты
   ```bash
    pytest -v
      ```