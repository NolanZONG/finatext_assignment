import sys
import json
import jwt
from cryptography.hazmat.primitives import serialization

# pip install cryptography pyjwt

RSA_JWT_ALGS = ["RS256", "RS384", "RS512", "PS256", "PS384", "PS512"]

RSA_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 validate.py jwts.txt")
        sys.exit(1)

    jwts_path = sys.argv[1]
    priv = serialization.load_pem_private_key(
        RSA_PRIVATE_KEY,
        password=None,
    )
    pub = priv.public_key()  # 用对应公钥验签（判断“是不是这把私钥签的”）

    with open(jwts_path, "r", encoding="utf-8") as f:
        tokens = [line.strip() for line in f if line.strip()]

    matched = 0
    for line_no, tok in enumerate(tokens, 1):
        # 解析 header（不校验）以减少尝试
        try:
            header = jwt.get_unverified_header(tok)
        except Exception:
            continue

        alg = header.get("alg")
        # 只关注 RSA 系列；HS/none 直接跳过
        if alg in ("HS256", "HS384", "HS512", "none", None):
            continue

        candidates = [alg] if alg in RSA_JWT_ALGS else RSA_JWT_ALGS

        for a in candidates:
            try:
                claims = jwt.decode(
                    tok,
                    pub,
                    algorithms=[a],
                    options={
                        "verify_signature": True,
                        "verify_exp": False,  # CTF 常见过期，先关；需要严格就 True
                        "verify_aud": False,
                        "verify_iss": False,
                    },
                )
                matched += 1
                print(f"\n=== MATCH #{matched} (line {line_no}, alg={a}) ===")
                print("header:", json.dumps(header, ensure_ascii=False))
                print("claims:", json.dumps(claims, ensure_ascii=False, indent=2))
                break
            except jwt.exceptions.InvalidSignatureError:
                # 签名不匹配：最常见，安静跳过
                pass
            except jwt.exceptions.PyJWTError:
                # 其他 JWT 相关错误（格式问题等），也跳过
                pass

    print(f"\nDone. Matched tokens: {matched}/{len(tokens)}")

if __name__ == "__main__":
    main()
