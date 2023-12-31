# Проект для опроса приборов учета электроэнергии и заполнения базы данных.

Этот проект представляет собой веб-приложение на основе Django и Django REST Framework для управления и мониторинга приборов учета электроэнергии.

## Клонирование проекта

Чтобы склонировать проект, выполните следующую команду:

```bash
git clone https://github.com/ваш-username/название-репозитория.git
cd название-репозитория
```

## Установка зависимостей

Прежде чем начать, убедитесь, что у вас установлен Python и pip. Для установки зависимостей выполните:

``` 
pip install -r requirements.txt
``` 

## Запуск проекта

Создайте файл .env в корневой директории проекта и заполните его:
```
SECRET_KEY=cекретный ключ проекта
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<имя базы данных>
POSTGRES_USER=<пользователь бд>
POSTGRES_PASSWORD=<пароль бд>
DB_HOST=db
DB_PORT=5432
```
Выполните следующие команды для запуска проекта:
```
python manage.py makemigrations
python manage.py migrate
pyrhon manage.py createsuperuser
python manage.py runserver
```
Проект будет доступен по адресу http://127.0.0.1:8000/

Для опроса приборов учета необходимо запустить файл service.py

Все приборы учета находятся в одной сети (диапазон адресов 127.0.0.1:9000 - 127.0.0.1:65000)



## Использование Swagger

Вы можете использовать Swagger для документации и тестирования API. Документация Swagger доступна по адресу http://127.0.0.1:8000/api/swagger/.