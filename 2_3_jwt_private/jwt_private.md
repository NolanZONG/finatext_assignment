# JWT - RSAの公開鍵/秘密鍵の性質 (12点)
## Question
次のファイル `jwts.rand2.txt` に、それぞれ異なる公開鍵/秘密鍵のペアで署名されたJWTが保存されています。

この中から、次の秘密鍵で署名されたJWTを見つけてください。
```
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAtv5yWUn9w2K1hIrEEkygzvdZJG7bPuPMO80sMskRyu1yOh25
Tk/Mcwmfxkuy3+HyPnBIi6G29e9crvxlo1qYjvhmtvuqVJkwnhhXTyRhQZ7No2LL
gM18BoSBBci8mrCxiHvyhVx1asdcXAZYyT3XpaRUMgi9xeUoOIFDutIOBXPJWJjv
hOeuH2KsYCLKxIuayyMlIuX2x21oSQ3CpNiG8o3QM6WU7IrIFypFAe9Kt5WqFt3S
9+BlLsGy2Gf49y7UMNUpoijuDAyX09cyus/XaVM6eacFHMEgqk9N9cjiflx8D5Xu
Z2oEZdsCLxC8fB8D43LP0yXO3xdEjw9mAbOiKQIDAQABAoIBAQCiPfwyD/juV0Dq
T4HBW7EjbofZVnQKUTuNNb5fFIgy68zfm+TkermgsMK4s/rWpmP5WeHn8qvdZqg8
+MhASZ2C/NdMmtqMgPlq4dfe8jlMTbiyiHA3NXgl6yrdbvlRCSGOCZ6fALeVwUWw
zWvAmJTuZkDDz545q4+6cVkUdRI7X8gzSLH4NPscAVLeUsYkEYXjtg74fKfeQLyp
Q1wAuaa7qJXZV8RuYmU3eAY+PYBbL9BoDmt64w9y0euZkO1BY7U/xPvUkyPvlnH9
mB9GBJnNSRSPim5dpK4LtyIFb3wE8Ld9pFuNASVWTitTmmLDQ6QqwaIll+II33HL
oiDS+GQ1AoGBAO+ww9yLPTle+FW/gZZjqMxASrsFf8QiEt1WSQcCLqSPRZK52z5C
G46ldudtqPZmjM+XeXeQNbrba/FLcm3dMir2QhRQKF8GHYRJe/vxCu9H1sE5pCAv
mOYwJd1GaxwdncUmLJ3PzbFjG3JDttjveeOQw/khzNSg/PVfPgkjH8xvAoGBAMNy
EY96y9DFhjOKhLtvYNA4Tpj5A2HyeY9ijYOAIeEPcCZzhcj3F5BIjJvc8gV8EMFC
/TFGccWDrIo849HN/t61e4t1uGOfZ4miQMH2gIHay5/z0TAvrQwsupYpranhFCr2
vDj+OlU+FEZCbdCUWVlFVG6EJw6M0cO86Pi2KXbnAoGBAOMoJRc4ppdel/+79PYw
EOMx8yD3fzTEDhjSE3ee69FtLsR1e4CvaipwShXeaYjLe5uptKZJd4JVPSF7HUFd
ppPsuodByGD2DLc4ZVZKBNDsxmxtUkxmj4NoEhp5CD2nG8Sh/xq4u/nnMTXDUuCZ
ZGz036WWEOdagyGQV9yU+yflAoGAc093gNmIKpJ/TSVqjlN2ISM3bBVuo3k1sx0I
NQ+B7ZD4MBd0VU9DPcMwAj1nJUk/cWaej1Xqhgfb4mtuVjhdKPSWAX/g3BYONive
XRGcXADEpohpYS6fwFEbfMD2TwYWqgqMnmuP6v8HYzSKKcd8t6ip2dJqYLFAiWWJ
ZkPDTv0CgYEA5O51BBy806tayUANAErYcyKY7TVpPcrtgMfcLl0/iW0dd19i8afb
8pT2XRVG8nPpVg6meNq12pL4bYrKPohfsMZSL3FckDixSqflP6hza4l682YuEC3h
NEpbZdj0zkZnBMazjmdWxVXPyNmF7K3Eo4gPIYiBzfZgPPfWGxdg42Y=
-----END RSA PRIVATE KEY-----
```
発見したJWTのClaimから、flagを取得してください。
(該当の秘密鍵で署名されていないJWTのClaimから取得できるflagはダミーです。)

## Answer
```
=== MATCH #1 (line 424, alg=PS256) ===

header: {"alg": "PS256", "typ": "JWT"}

claims: {

  "flag": "f1nat3xthd{0ad9dc6b-9e07-4e0f-b142-ff170e6d2ac1}"


}
```