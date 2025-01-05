from selenium.webdriver.common.by import By

# Поле имя
FIELD_NAME = (By.XPATH, '//label[text()="Имя"]/../input')

# Поле email
FIELD_EMAIL = (By.XPATH, '//label[text()="Email"]/../input')

# Поле пароль
FIELD_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/../input')

# Кнопка Зарегистрироваться
BUTTON_REGISTER = (By.XPATH, '//button[text()="Зарегистрироваться"]')

# Сообщение о некорректном пароле
MESSAGE_INCORRECT_PASS = (By.XPATH, '//p[text()="Некорректный пароль"]')

# Кнопка Войти
BUTTON_LOGIN = (By.XPATH, '//form/button')

# Ссылка Войти
LINK_LOGIN = (By.LINK_TEXT, 'Войти')

# Кнопка Войти в аккаунт
BUTTON_LOGIN_IN_ACCOUNT = (By.XPATH, '//section[2]/div/button')

# Отображение текста Войти после регистрации
MESSAGE_AFTER_REGISTER = (By.XPATH, '//a[text()="Войти"]')

# Кнопка Выход в профиле
BUTTON_LOGOUT_IN_PROFILE = (By.XPATH, "//button[text()='Выход']")

# Кнопка Конструктор
BUTTON_CONSTRUCTOR = (By.XPATH, '//li/a')

# Кнопка Личный кабинет
BUTTON_ACCOUNT = (By.LINK_TEXT, 'Личный Кабинет')

# Раздел Булки
SECTION_BUNS = (By.XPATH, "//span[text() = 'Булки']")

# Раздел Начинки
SECTION_FILLINGS = (By.XPATH, "//span[text() = 'Начинки']")

# Раздел Соусы
SECTION_SAUCES = (By.XPATH, "//span[text() = 'Соусы']")
