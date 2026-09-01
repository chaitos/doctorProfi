# DoctorProfi 

Веб-сайт медицинского центра (акушерство и гинекология) на Django: витрина услуг, расписание врачей, страница цен и онлайн-запись на приём с сохранением заявок в базу данных.

## Возможности

- **Главная страница** с описанием клиники и преимуществ
- **Каталог врачей** с фильтрацией по доступности (`available=True`)
- **Расписание** приёма по каждому врачу
- **Страница цен** на услуги
- **Онлайн-запись на приём** — форма отправляется через AJAX и сохраняется в БД без перезагрузки страницы (ответ в формате JSON)
- **Админ-панель Django** для управления врачами и записями (кастомизированные `list_display`, инлайн-редактирование поля `available`)
- Адаптивная вёрстка с анимациями появления элементов при скролле (Intersection Observer)

## Стек

- Python 3 / Django 4.2
- SQLite (БД по умолчанию для разработки)
- HTML, CSS, vanilla JS
- Django Templates

## Структура проекта

```
doctorProfi/
├── doctorProfi/          # настройки проекта (settings, urls, wsgi/asgi)
└── profi/                # основное приложение
    ├── models.py          # модели Doctors и Appointment
    ├── views.py           # обработка страниц и формы записи
    ├── urls.py
    ├── admin.py           # настройка админ-панели
    ├── converters.py       # кастомный URL-конвертер
    ├── static/profi/      # css, js, изображения
    └── templates/profi/    # index, prices, schedule, blog
```

## Установка и запуск локально

```bash
git clone https://github.com/chaitos/doctorProfi.git
cd doctorProfi/doctorProfi

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

# создать файл .env (см. .env.example) и указать свой SECRET_KEY

python manage.py migrate
python manage.py createsuperuser   # чтобы зайти в /admin/
python manage.py runserver
```

Сайт будет доступен на `http://127.0.0.1:8000/`, админка — на `http://127.0.0.1:8000/admin/`.

## Модели данных

**Doctors** — имя, специализация, телефон, график работы, email, флаг доступности для записи.

**Appointment** — заявка пациента: имя, телефон, email, дата и время приёма, комментарий, ссылка на врача.

## О проекте

Учебный pet-проект, реализующий типовой сайт-визитку клиники с базовой CRUD-логикой через Django ORM и админ-панель. Написан в процессе изучения Django.

## Возможные улучшения

- [ ] Валидация формы записи на бэкенде (сейчас поля берутся из `POST` без проверки)
- [ ] Проверка занятости слота времени у врача
- [ ] Тесты (`tests.py` сейчас пустой)
- [ ] Docker-контейнеризация
- [ ] Переход на PostgreSQL для продакшена
