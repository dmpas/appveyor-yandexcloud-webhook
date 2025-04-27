# appveyor-yandexcloud-webhook
Вебхук для деплоя из аппвеёра в яндекс-облако

Требуется указание переменных среды:
* `BUCKET_NAME` - имя корзины
* `AWS_ACCESS_KEY_ID` - идентификатор ключа S3 для доступа к корзине
* `AWS_SECRET_ACCESS_KEY` - секретный ключ S3 для доступа к корзине

Формируется ссылка вида

`https://storage.yandexcloud.net/{Имя корзины}/{Имя проекта в AppVeyor}/{ветка}/{ИД платормы (или имя образа)}/{Имя артефакта}`


# Ссылки

https://www.appveyor.com/docs/environment-variables/

https://www.appveyor.com/docs/deployment/webhook/
