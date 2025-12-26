# HTTP - APIサーバーの構築(ログイン) (8点)
## Question
以下の仕様で定義されたAPIエンドポイントがあります。

* Base URL: https://skill-test.st8.workers.dev
* Endpoint: POST `/v1/q3-2/agent`
* Request
    * Header
        * Content-Type: `application/json`
    * Body
        * target: `string (required)` example: http://example.com/api/

このエンドポイントに正しくリクエストを送信すると、targetで指定したサーバーに対して以下の仕様のリクエストが送信されます。

* Base URL: targetで指定したURL
* Endpoint: PUT `/login`
* Request
    * Header
        * Content-Type: `application/json`
    * Body
        * username: `string`
        * password: `string`

このリクエストに対して、以下の仕様を満たすレスポンスを返却してください。

* Response
    * Header
        * Content-Type: `application/json`
    * Body
        * token: `string`

このとき token の値は、リクエストに含まれる username と password を文字列結合し、SHA1のChecksumを計算した値としてください。
例えば、username: admin, password: thisispassword の場合は 8368890114e5e84ade36e721e8cf29b1207004d5 となります。

正しいレスポンスを返却できると、次は以下の仕様のリクエストが送信されます。

* Base URL: targetで指定したURL
* Endpoint: PUT /flag
* Request
    * Header
        * Content-Type: `application/json`
* Body
    * flag: `string`

このリクエストから、flagの値を取得してください。