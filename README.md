# Yatube API

В этом репозитории вы сможете найти API, которую можно использовать для блогов, социальных сетей и т.д.


## Реализованный функционал API:

 - Публикации
 - Комментарии
 - Группы
 - Подписки
 
 CRUD фундамент подготовлен для всех вышеупомянутых разделов. Настраивайте пермишены на ваше усмотрение.


Как запустить проект:

    Клонировать репозиторий и перейти в него в командной строке:
        git clone git@github.com:usancho/api_final_yatube.git
        cd yatube_api

    Cоздать и активировать виртуальное окружение:
        python3 -m venv env
        source env/bin/activate

    Установить зависимости из файла requirements.txt:
        python3 -m pip install --upgrade pip
        pip install -r requirements.txt

    Выполнить миграции:
        python3 manage.py migrate

    Запустить проект:
        python3 manage.py runserver


Примеры запросов.

        GET http://127.0.0.1:8000/api/v1/posts/

        [
            {
                "id": 1,
                "author": "user1",
                "text": "Сегодня я спал 12 часов.",
                "pub_date": "2022-12-23T08:39:54.912181Z",
                "image": null,
                "group": null
            },
            {
                "id": 2,
                "author": "user1",
                "text": "Вчера я не спал.",
                "pub_date": "2022-12-23T08:40:12.882554Z",
                "image": null,
                "group": null
            },
            {
                "id": 3,
                "author": "user1",
                "text": "Позавчера я спал 4 часа.",
                "pub_date": "2022-12-23T08:40:31.196120Z",
                "image": null,
                "group": null
            },
        ]

        GET http://127.0.0.1:8000/api/v1/groups/

        [
            {
                "id": 1,
                "title": "Готовка",
                "slug": "1",
                "description": "Обсуждаем готовку!"
            },
            {
                "id": 2,
                "title": "Спорт",
                "slug": "2",
                "description": "Обсуждаем спорт!"
            },
            {
                "id": 3,
                "title": "Музыка",
                "slug": "3",
                "description": "Обсуждаем музыку"
            },
        ]
