# Сервис сокращения ссылок YaCut
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd60)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.3.x/)
[![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)

Финальный проект спринта: сервис YaCut
Веб-приложение на основе Flask, оформленное как пакет Python

## Технологии:
- Python 3.9
- Flask 3.0.2
- Flask-SQLAlchemy 3.1.1
- Alembic 1.12.0
- Flask-WTF 1.2.1

## Возможности
Сервис способен:
* генерировать короткие ссылки и связывать их с исходными длинными ссылками;
* переадресовывать пользователя на исходный адрес при обращении к коротким ссылкам.

Сервис может взаимодействовать с пользоваетелем двумя способами
1. Через интерфейс с формой на главной странице `host/`

2. Через API с двумя эндпойнтами: `host/api/id/` и `host/api/id/<short_id>/`

### Работа API

Примеры запросов к API, варианты ответов и ошибок приведены в спецификации `openapi.yml` Спецификация находится в репозитории yacut.

### Работа базы данных

Взаимодействие с базой данных осуществляется через ORM-модуль `Flask-SQLAlchemy`
При разворачивании проекта потребуется в консоли применить миграции.


## Запуск локально

1. Достаточно склонировать репозиторий, развернуть виртуальное окружение:

```
git clone
cd yacut
python3 -m venv venv

```
* Если у вас Linux/macOS
    ```
    source venv/bin/activate
    ```

* Если у вас windows
    ```
    source venv/scripts/activate
    ```

2. Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Заменить секретный ключ в файле `.env.example` и переименовать файл в `.env`

4. Инициализировать базу данных
```
flask db upgrade
```
### Готово!
Приложение готово к запуску командой
```
flask run
```

## Автор проекта
### [Преображенский Глеб](https://github.com/Gleb-Preob)
