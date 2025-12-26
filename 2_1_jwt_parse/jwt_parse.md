# JWT - Payloadのからの値の取得 (4点)
## Question
次の文字列は、ある一般的な方法で生成されたJSON Web Token (JWT)です。
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbGFnIjoiZjFuYXQzeHRoZHs4MDExODE0Yi00NzBjLTRmM2MtYWE2ZS0yMTVhYThkYjk5MjR9In0.-LoKWOcI9J1xbnul1YziIxjUziIIS8jZMfpB1HPx4BI
```
このJWTのClaimから、flagを取得してください。
## Answer
```
nan.so@VVHG0G6H96 Downloads % echo "eyJmbGFnIjoiZjFuYXQzeHRoZHs4MDExODE0Yi00NzBjLTRmM2MtYWE2ZS0yMTVhYThkYjk5MjR9In0" | base64 -d
```
## Flag
```json
{"flag":"f1nat3xthd{8011814b-470c-4f3c-aa6e-215aa8db9924}"}
```