# stdx-server
*Установка виртуального окружения должна работать через батник(но это не точно)*

Запуск локалки происходит через start_server.bat
#
<b>API Requests:</b>

1./api/v1/tasks/ - Все таски (GET, POST)

2./api/v1/tasks/1 -  - Отедльный таск (GET, PUT, DELETE)

3./api/v1/category/ - Все предметы

4./api/v1/university/ - Все универы
#
<b>Если не робит с окружением</b>
Ставим питон от версии 3.9. Заходим в папку с проектом. в консоли пишем

*python pip install -r req.txt*

Для запуска сервера переходим в директорию *stdx* и пишем

*python manage.py runserver*
