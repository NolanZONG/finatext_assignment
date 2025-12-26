# HTTP - POSTリクエストの送信 (4点)
## Question
以下の仕様で定義されたAPIエンドポイントがあります。
* Base URL: https://skill-test.st8.workers.dev
* Endpoint: POST `/v1/q3-1/login`
* Request
    * Header
        * Content-Type: `application/json`
    * Body
        * username: `string (required)`
        * password: `string (required)`

このエンドポイントに、
* username: `admin`
* password: `supersecretpassword`

でリクエストを送信してください。

レスポンスに含まれるflagを取得してください。

## Answer
```
curl -X POST "https://skill-test.st8.workers.dev/v1/q3-1/login" \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{
    "username": "admin",
    "password": "supersecretpassword"
}'
```

## Flag
```json
{"token": "d97329d6c03c90a0c82bfec27e9427e796324861", "flag": "f1nat3xthd{8727d491-8190-4a3a-a937-d94a71d89c6c}"}
```