# HTTP - APIサーバーの構築(ローソク足) (16点)
## Question
### Overview
以下の仕様で定義されたAPIエンドポイントがあります。

* Base URL: https://skill-test.st8.workers.dev
* Endpoint: POST `/v1/q3-3/agent`
* Request
    * Header
        * Content-Type: `application/json`
    * Body
        * target: `string (required)` example: http://example.com/api/
このエンドポイントに正しくリクエストを送信すると、targetで指定したサーバーに対して以下の仕様のリクエストが送信されます。

* Base URL: targetで指定したURL
* Endpoint: GET `/candle`
* Request
    * Params
        * code: `string`
        * year: `int`
        * month: `int`
        * day: `int`
        * hour: `int`
このリクエストに対して、以下の仕様を満たすレスポンスを返却してください。

* Response
    * Header
        * Content-Type: `application/json`
    * Body
        * open: `int: 始値`
        * high: `int: 高値`
        * low: `int: 安値`
        * close: `int: 終値`
このとき、`open/high/low/close` の値は、後述する方法にて算出した数値を返却してください。

このリクエストが、毎回違うパラメータで3回送信されます。
3回のリクエスト全てに正しいレスポンスを返却できると、次は以下の仕様のリクエストが送信されます。

* Base URL: targetで指定したURL
* Endpoint: PUT `/flag`
* Request
    * Header
        * Content-Type: `application/json`
    * Body
        * flag: `string`
このリクエストから、flagの値を取得してください。

### open/high/low/closeの計算方法について
このCSVファイル `order_books.csv`
に、以下の仕様の架空の株銘柄のTick(株価の変動のデータ)が保存されています。

| Column | Type       | Description |
| :---   | :---       | :---        |
| time   | datetime   | Tickの時刻   |
| code   | string     | 株銘柄コード |
| price  | int        | 価格        |


このデータを元に、株銘柄毎の、時間足(1時間単位で集計したローソク足)を計算してください。

例えば、以下のようなデータから生成される 銘柄:`FTHD` 時間:`2021/12/22 10時` の時間足は `{open: 100, high: 170, low: 99, close: 156}` となります。
```
2021-12-22 09:59:59 +0900 JST,FTHD,98
2021-12-22 10:00:00 +0900 JST,FTHD,100
2021-12-22 10:02:43 +0900 JST,FTHD,101
2021-12-22 10:12:43 +0900 JST,FTHD,99
2021-12-22 10:22:43 +0900 JST,FTHD,104
2021-12-22 10:32:46 +0900 JST,FTHD,130
2021-12-22 10:43:10 +0900 JST,FTHD,150
2021-12-22 10:53:28 +0900 JST,FTHD,170
2021-12-22 10:55:43 +0900 JST,FTHD,156
2021-12-22 11:00:00 +0900 JST,FTHD,180
```

## Answer
### Installation
```
pip install "fastapi[standard]"
```
### Run
```
fastapi dev candle.py --host 0.0.0.0 --port 80
```
