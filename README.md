<a id="anchor"></a>
<div align=center>

  # Тестовое задание

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

</div>

## Описание тестового задания

```
    Требуется разработать простое API приложения на Django REST Framework, для работы
с которым используются 4 API endpoints по принципу CRUD.
    Допустим это будет личный блог, с одной моделью у которой есть поля: пользователь,
имя записи, текст, дата создания опубликована ли запись. 
    Важно: не использовать ModelViewSet и viewsets,  допускается использование generics
APIView, но в приоритете базовое APIView.
    Желательно, но не обязательно: 
        1. Предусмотреть права, чтобы только пользователь или администратор мог удалять
            или изменять запись.
        2. Написать тесты для разработанного API.
        3. Добавить OpenAPI описание с помощью drf-spectacular.

Стэк: python 3.10 и выше, база данных на свое усмотрение.
```

### Технологии

Python 3.10.11

Django 4.2
Django REST Framework 3.14

Database SQLite/PostgreSQL

<details>
<summary>
<h4>Запуск проекта</h4>
</summary>

<br>

~~~
склонировать проект git clone git@github.com:JustLight1/test-ReAction.git
~~~
- При первом запуске для функционирования проекта обязательно установить виртуальное окружение, установить зависимости,  выполнить миграции:

```
python -m venv venv

source venv/Scripts/activate

python -m pip install --upgrade pip
```
- Установите зависимости из файла requirements.txt

```
pip install -r requirements.txt
```
- Выполните миграции БД. Из папки backend с файлом manage.py выполните команду:
```
python manage.py makemigrations
python manage.py migrate
```
- Для создания суперюзера из папки backend с файлом manage.py выполните команду:
```
python manage.py createsuperuser
```

- Для запуска сервера из папки backend с файлом manage.py выполните команду:

```
python manage.py runserver
```
</details>


<details>
<summary>
<h4>Шаблон наполнения env-файла</h4>
</summary>

<br>

```env
  DEBUG=True/False - Влияет так же на выбор БД SQLite/PostgreSQL
  SECRET_KEY=''
```

</details>

## Контакты:

**Форов Александр** 

[![Telegram Badge](https://img.shields.io/badge/-Light_88-blue?style=social&logo=telegram&link=https://t.me/Light_88)](https://t.me/Light_88) [![Gmail Badge](https://img.shields.io/badge/forov.py@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:forov.py@gmail.com)](mailto:forov.py@gmail.com)