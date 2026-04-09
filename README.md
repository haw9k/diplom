# UI-каркас + авторизация + точки встройки A1-A7

Этот проект собран из предыдущей курсовой, но из него оставлены только:
- UI-каркас Django
- авторизация через `django-allauth`
- шаблоны входа, регистрации, сброса и смены пароля
- страницы-заглушки для статистики, достижений и пользователей

## Что уже вычищено
- старая бизнес-логика по VK, hh.ru и БД курсовой
- жёстко зашитые SMTP-учётки
- модели `managed = False`, завязанные на старую базу
- скрипты старого сбора данных

## Куда вставлять код по этапам
- **A1**: `pipeline/a1_collection/service.py`
- **A2**: `pipeline/a2_preprocessing/service.py`
- **A3**: `pipeline/a3_ml/service.py`
- **A4**: `pipeline/a4_validation/service.py`
- **A5**: `pipeline/a5_deployment/service.py`
- **A6**: `pipeline/a6_analytics/service.py`
- **A7**: `pipeline/a7_monitoring/service.py`

## Куда подключать результаты в UI
- Главная страница: `ui/views.py -> home_view`
- Статистика: `ui/views.py -> stats_view`
- Достижения: `ui/views.py -> achievements_view`
- Список выпускников: `ui/views.py -> users_view`
- Шаблоны интерфейса: `ui/templates/ui/*.html`

## Запуск
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Что делать дальше
1. Реализовать A1-A7 в папке `pipeline/`.
2. После каждого этапа подключать реальные результаты в `ui/views.py`.
3. Когда понадобятся REST API и Airflow DAG, добавить отдельные пакеты `api/` и `dags/`.
