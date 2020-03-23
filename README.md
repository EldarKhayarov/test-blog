# Тестовый блог
## Запуск
Для запуска сперва небходимо создать конфиг-файл 
с именем `config.json` в корне проекта.

В файле должны храниться занчения следующих переменных:

  - SECRET_KEY
  - DEBUG
  - ALLOWED_HOSTS
  - DB_NAME
  - DB_USER
  - DB_PASSWORD
  - DB_HOST - тут следует присвоить имя `db`
  - DB_PORT
  - LANGUAGE_CODE
  - TIME_ZONE
  - USE_I18N
  - USE_L10N
  - USE_TZ
  - STATIC_URL
  - EMAIL_HOST
  - EMAIL_HOST_USER
  - EMAIL_HOST_PASSWORD
  - EMAIL_PORT
  - EMAIL_USE_TLS
  - EMAIL_USE_SSL
  
Перед первым запуском необходимо вручную сделать миграции:
        
        docker-compose run app python manage.py migrate
        
Если необходим админ, ввести следующую команду, затем указав данные админа:

        docker-compose run app python manage.py createsuperuser
        
Примечание: если после выполнения предыдущей команды контейнер не приостанавливается, 
это следует сделать комбинацией CTRL+C.

Команда запуска:

        docker-compose up
