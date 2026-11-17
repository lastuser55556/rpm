# DevTools для тестировщика

Запуск локального примера: `python3 server.py`. Страница открывается по адресу http://127.0.0.1:8765.

1. На вкладке Network включаю фильтр Fetch/XHR и нажимаю Valid request. В запросе POST /api/quote на вкладке Payload виден quantity=2, статус 200, ответ содержит total_kopecks=5000.
2. Нажимаю Invalid request. В Payload виден quantity=0, ответ 400 содержит invalid_quantity. Статус 400 ожидаем, потому что цена рассчитывается только для количества 1–10.
3. На вкладке Elements нахожу pre#result и сверяю его текст с серверным ответом. Редактирование DOM в инспекторе меняет только открытую страницу.
4. Для диагностики JavaScript можно поставить точку остановки в функции show и проверить quantity и response.status. Network показывает факт и содержание HTTP-запроса, Sources — место, где этот запрос создаётся.

| Проверка | Статус | Ответ |
|---|---:|---|
| quantity=2 | 200 | total_kopecks=5000 |
| quantity=0 | 400 | invalid_quantity |
| quantity=11 | 400 | invalid_quantity |
| quantity=true | 400 | invalid_quantity |

Ответы в таблице подтверждены локальными HTTP-запросами к серверу. Порядок действий в DevTools позволяет повторить первые два запроса через браузер.
