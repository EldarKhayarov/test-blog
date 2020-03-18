# Тестовый блог
## Запуск
Для запуска сперва небходимо создать конфиг-файл:

  - либо с именем `config.json` в корне проекта
  - либо с произвольным именем в формате json с указанием
   полного пути в переменной окружения `CONFIG_PATH`

В файле должны храниться занчения следующих переменных:

  - SECRET_KEY
  - DEBUG
  - ALLOWED_HOSTS
  - DB_NAME
  - DB_USER
  - DB_PASSWORD
  - DB_HOST
  - DB_PORT
  - LANGUAGE_CODE
  - TIME_ZONE
  - USE_I18N
  - USE_L10N
  - USE_TZ
  - STATIC_URL
