# dj_goosheets

Данные поступают из документа Google Sheets при помощи Google API, добавляются в БД в том же виде что и в источнике с добавлением колонки "Стоимость в рублях". Получите google API в json файле и положите в папку app c названием 'creds.json'
Создайте env в дирректории app: python3.9 -m venv env
Активируйте: source env/bin/activate
Установите django: `pip install django`
- `python manage.py makemigrations`
- `python manage.py migrate`

Создаем образ:
- `docker build .`

Соберем новый образ и запустим два контейнера:
- `docker-compose up -d --build`

Запустим миграцию:
- `docker-compose exec web python manage.py migrate --noinput`

Убедимся, что все таблицы Django по умолчанию были созданы:
- `docker-compose exec db psql --username=django_user --dbname=django_db`

Вы также можете проверить, что том (volume) был создан, запустив команду:
- `docker volume inspect django-on-docker_postgres_data`
Вы должны увидеть что-то похожее на:

[
    {
        "CreatedAt": "2020-06-13T18:43:56Z",
        "Driver": "local",
        "Labels": {
            "com.docker.compose.project": "dj_docker",
            "com.docker.compose.version": "1.25.4",
            "com.docker.compose.volume": "postgres_data"
        },
        "Mountpoint": "/var/lib/docker/volumes/django-on-docker_postgres_data/_data",
        "Name": "dj_docker_postgres_data",
        "Options": null,
        "Scope": "local"
    }
]

Обновим локальные права доступа к файлу:
- `chmod +x app/entrypoint.sh`

Проверьте все снова:
Пересоберем заново образы->
Запустим контейнеры->
Перейдем на страницу http://localhost:8000/

![alt text](https://github.com/Mitsufiro/dj_goosheets/blob/master/google_sheets.png)
БД создана на основе PostgreSQL,данные для перевода $ в рубли получаются по курсу ЦБ РФ автоматически.
Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме учитывается, что строки в Google Sheets таблицы могут удаляться, добавляться и изменяться.
Весь функционал в одностраничном Django web-приложении которое обернуто в Docker контейнер
![alt text](https://github.com/Mitsufiro/dj_goosheets/blob/master/Table.png)
