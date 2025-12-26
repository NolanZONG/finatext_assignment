#  Network - DKIM (8点)
## Question
以下のような DKIM-Signature が付与されたメールを受信した際、メールクライアントは所定の場所から公開鍵を取得してメールの検証を行います。
```
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=st.fntxt.co; s=dk4419; ..snip..
```
本来公開鍵が設置されている場所に、代わりにflagをセットしてあるので、そこからflagを取得してください。

## Answer & Flag
```
dig TXT dk4419._domainkey.st.fntxt.co


"v=DKIM1;k=rsa;p=f1nat3xthd{eb690513-0b2b-45a4-b6a3-591c56ac1a91}"
```