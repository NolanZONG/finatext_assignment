# Container - コンテナの実行 (4点)
## Question
Docker Hubから、以下のコンテナイメージを取得し、実行してください。
```
stajima/skill-test:v1_q1-1
```
尚、このコンテナイメージは以下のDockerfileでビルドされています。
```
FROM alpine
COPY flag.txt /
ENTRYPOINT ["/bin/cat", "/flag.txt"]
```
ファイルコンテナイメージの/flag.txtからflagを取得してください。
## Answer
```
docker run --rm stajima/skill-test:v1_q1-1
```
## Flag
```
f1nat3xthd{f778f18c-ebe3-4678-8aa2-853d15b379b6}
```
# Container - コンテナ上の任意のコマンドの実行 (8点)
## Question
Docker Hubから、以下のコンテナイメージを取得し、実行してください。
```
stajima/skill-test:v1_q1-2
```
尚、このコンテナイメージは以下のDockerfileでビルドされています。
```
FROM alpine
COPY flag.txt /
ENTRYPOINT ["/bin/echo", "hello"]
```
ファイルコンテナイメージの/flag.txtからflagを取得してください。
## Answer
```
docker run --entrypoint /bin/cat stajima/skill-test:v1_q1-2 /flag.txt
```
## Flag
```
f1nat3xthd{b82df727-593a-46cc-9949-dabe8b8c10a7}
```
# Container - コンテナ上のファイルの取得 (12点)
## Question
Docker Hubから、以下のコンテナイメージを取得し、実行してください。
```
stajima/skill-test:v1_q1-3
```
尚、このコンテナイメージは以下のDockerfileでビルドされています。
```
FROM gcr.io/distroless/static
COPY flag.txt /
ENTRYPOINT ["/bin/sh"]
```
ファイルコンテナイメージの/flag.txtからflagを取得してください。
## Answer
```
docker create --name ctf_tmp stajima/skill-test:v1_q1-3

docker cp ctf_tmp:/flag.txt .
```
## Flag
```
f1nat3xthd{7d374833-4dcb-4a66-9aa7-8c3a7ff737de}
```