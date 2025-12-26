import sys
import json
import jwt
from cryptography.hazmat.primitives import serialization

SSH_RSA_PUB = r"""ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC6eLDuYM4TKIKRvc5MSCPGiMSi7PYmbPMAkX6QbNc3PZtlvDjIL9ZYVsrVgw7FIvzpwzouqTV6K401AcRh7j24AXxNaH3OeC4uyx8u1u0mfxUB6DB6FjfjZsD46uqQvj6/GwZGLPkZ8Gyduqbi776Pb9LuBEyZo6wIGjQsHbELJmou4e2SeBEU6yF6MiFQ+DGK2xl6vikjslYzwXSCj7pD2hoVAc5nS5wjU5cf6rerDBcYmvjkN7qvBM+JkSUoWRjLbbyqoJJIHRQHQZay6HFOc88wCY+KHwnPg7+QWTNMpQgFDBQ0Rran1Mm/LH6HK7f0mT8Dl99zCBI/6BMKyVA5"""

# 读取 OpenSSH 公钥（ssh-rsa ...）成 cryptography 公钥对象
pubkey = serialization.load_ssh_public_key(SSH_RSA_PUB.encode("utf-8"))

# RSA 公钥 → 只需要尝试 RSxxx
ALGS = ["RS256", "RS384", "RS512"]

def try_decode(token: str):
    # 先把 header 解出来看看（不校验）
    try:
        header = jwt.get_unverified_header(token)
    except Exception:
        return None

    # 如果对方 header 声称是 HS256/none 等，直接跳过（用 RSA 公钥验不了）
    alg = header.get("alg")
    if alg in ("HS256", "HS384", "HS512", "none", None):
        return None

    # 优先用 header.alg，如果不在列表就全试
    candidates = [alg] if alg in ALGS else ALGS

    for a in candidates:
        try:
            claims = jwt.decode(
                token,
                pubkey,
                algorithms=[a],
                options={
                    "verify_signature": True,
                    "verify_aud": False,
                    "verify_iss": False,
                    "verify_exp": False,
                },
            )
            return a, header, claims
        except Exception:
            pass
    return None

def main():
    # 用法：python3 scan_jwts.py jwts.txt
    path = sys.argv[1] if len(sys.argv) > 1 else None
    if not path:
        print("Usage: python3 validate.py jwts.txt")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        tokens = [line.strip() for line in f if line.strip()]

    found = 0
    for i, tok in enumerate(tokens, 1):
        res = try_decode(tok)
        if not res:
            continue
        alg, header, claims = res
        found += 1
        print(f"\n=== VALID JWT line #{i} (alg={alg}) ===")
        print("header:", json.dumps(header, ensure_ascii=False))
        print("claims:", json.dumps(claims, ensure_ascii=False, indent=2))

    print(f"\nDone. Valid tokens found: {found}")

if __name__ == "__main__":
    main()
