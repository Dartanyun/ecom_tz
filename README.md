# ecom_tz
Тестовое задание по вакансии Backend-developer в компанию Ecom.

## Стек технологий
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)

### Подготовка проекта к запуску

#### `3` и `4` пункты для локального запуска

1. *Склонируйте репозиторий и перейдите в него*:

    ```sh
    git clone https://github.com/Dartanyun/ecom_tz.git
    ```
    ```sh
    cd ecom_tz/
    ```
---
2. *Для работы с PostgreSQL*:

    * Создайте в директории `ecom/` и `ecom/infra/` файл `.env` командой:

        ```sh
        touch .env
        ```
        > Заполните оба файла переменными по примеру файла `.env.example` из этой же директории.
---
3. *Создайте и активируйте виртуальное окружение*:

    ```sh
    python -m venv venv
    ```
    - Если у вас Linux/macOS
        ```sh
        source venv/bin/activate
        ```

    - Если у вас windows
        ```sh
        source venv/scripts/activate
        ```
---
4. *Обновите pip и установите зависимости*:

    ```sh
    python -m pip install --upgrade pip
    ```
    ```sh
    pip install -r requirements.txt
    ```

### Для локального запуска используйте инструкцию

1. *Выполните миграции*:

    * Создайте миграции
        ```sh
        python manage.py makemigrations
        ```

    * Инициализируйте миграции
        ```sh
        python manage.py migrate
        ```

    * Примените миграции
        ```sh
        python manage.py migrate
        ```
---
2. *Наполните базу данными*:

    Команда для загрузки данных в бд:

    ```sh
    python manage.py loaddata */fixtures/*.json
    ```
    Также из фикстур создается базовая admin запись со следующими данными.

    email: admin@admin.ru
    password: admin
---
3. *Локальный запуск*:

    ```sh
    python manage.py runserver
    ```
---
### Для запуска в Docker-контейнере используйте инструкцию

1. *Запустите сборку контейнеров*:

    ```sh
    docker compose -f ecom/infra/docker-compose.yaml up -d --build
    ```
2. *Для остановки контейнера*:
    ```sh
    docker compose -f ecom/infra/docker-compose.yaml down
    ```
---
