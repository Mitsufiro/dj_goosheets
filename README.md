# dj_goosheets

Данные поступают из документа Google Sheets при помощи Google API, добавляются в БД в том же виде что и в источнике с добавлением колонки "Стоимость в рублях". 
![alt text](https://github.com/Mitsufiro/dj_goosheets/blob/master/google_sheets.png)
БД создана на основе PostgreSQL,данные для перевода $ в рубли получаются по курсу ЦБ РФ автоматически.
Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме учитывается, что строки в Google Sheets таблицы могут удаляться, добавляться и изменяться.
Весь функционал в одностраничном Django web-приложении которое обернуто в Docker контейнер
![alt text](https://github.com/Mitsufiro/dj_goosheets/blob/master/Table.png)
