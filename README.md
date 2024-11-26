# Курсовая работа №7. DRF
Трекер полезных привычек.

Сервер запускается командой - "python manage.py runserver"
Команды для управления сервером:

Запуск отложенных и периодических задач:
1. Запуск обработчика очереди (worker) для получения задач и выполнения их выполняется командой:
celery -A config worker -l INFO
Где:
config — директория с конфигурацией Django-проекта;
worker — тип запуска, данный параметр запускает обработчик задач из очереди;
-l INFO — уровень логирования.
!!! Обратите внимание, что для Windows при указании обработчика событий необходимо добавить флаг 
-P eventlet, для этого установите модуль eventlet==0.38.0!!!
2. Запуск Celery worker и планировщика Celery beat.
Чтобы использовать периодические задачи, нужно запустить не только Celery worker, но и планировщик Celery beat. Выполните следующую команду в командной строке:
celery -A config worker —loglevel=info
celery -A config beat —loglevel=info
Это запустит Celery worker и планировщик Celery beat, которые будут совместно работать для выполнения периодических задач.

Настройка и примеры работы с Celery: https://docs.celeryq.dev.
Работа и настройка celery-beat: https://django-celery-beat.readthedocs.io/. 
Официальный сайт Redis, на котором можно найти инструкции по установке, а также документацию по работе с консольным интерфейсом: https://redis.io/. 

Безопасность
Для проекта настроен CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере.
Сайт - https://pypi.org/project/django-cors-headers/

Flake8 — это инструмент для проверки стиля и качества кода на Python. 
Он позволяет просканировать код проекта и обнаружить в нём стилистические ошибки и нарушения различных конвенций кода
Установка flake8:
python -m pip install flake8.
Чтобы запустить Flake8 на Python, нужно ввести в командной строке:
flake8 config

Если вы пользуетесь pip (менеджер установки пакетов), то все зависимости можно установить с файла 
[requirements.txt](requirements.txt), выполнив команду в командной строке: pip install -r requirements.txt. 

Для сохранения фикстур используем команду:
python -Xutf8 manage.py dumpdata habits(имя приложения) --indent 2 -o habits.json

Для работы с тестами используется библиотека coverage==7.6.8

Для выполнения тестов используем команду:
coverage run --source='.' manage.py test

Для статистики покрытия тестами проекта используем команду:
coverage report