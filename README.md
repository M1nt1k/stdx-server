# stdx-server

<b>API Requests:</b>

0. /api/v2/ - Получаем все ссылки, которые есть (GET)

1. /api/v2/users/ - Все юзвери (GET, POST)

2. /api/v2/users/<pk> - Отдельный юзверь (GET, PUT, DELETE)

3. /api/v2/tasks/ - Все таски (GET, POST)

4. /api/v2/tasks/<pk> - Отдельный таск (GET, PUT, DELETE)

5. /api/v2/files/ - Все таски (GET, POST)

6. /api/v2/files/<pk> - Отдельный файл (GET, PUT, DELETE)

7. /api/v2/categories/ - Все предметы (GET)

8. /api/v2/universities/ - Все универы (GET)
#
<b>Запуск сервера</b>
Ставим питон от версии 3.9. Заходим в папку с проектом. В консоли пишем:

*python -m venv .venv*

*.venv\Scripts\activate.ps1*

*python -m pip install -U pip*

*pip install -r req.txt*

После установки django запускаем сервер:

*cd stdx*

*python manage.py runserver*
