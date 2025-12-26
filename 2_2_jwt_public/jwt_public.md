# JWT - 公開鍵による検証 (8点)
## Question
次のファイル `jwts.rand.txt` に、それぞれ異なる公開鍵/秘密鍵のペアで署名されたJWTが保存されています。

この中から、次の公開鍵で正しく検証できるJWTを見つけてください。
```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC6eLDuYM4TKIKRvc5MSCPGiMSi7PYmbPMAkX6QbNc3PZtlvDjIL9ZYVsrVgw7FIvzpwzouqTV6K401AcRh7j24AXxNaH3OeC4uyx8u1u0mfxUB6DB6FjfjZsD46uqQvj6/GwZGLPkZ8Gyduqbi776Pb9LuBEyZo6wIGjQsHbELJmou4e2SeBEU6yF6MiFQ+DGK2xl6vikjslYzwXSCj7pD2hoVAc5nS5wjU5cf6rerDBcYmvjkN7qvBM+JkSUoWRjLbbyqoJJIHRQHQZay6HFOc88wCY+KHwnPg7+QWTNMpQgFDBQ0Rran1Mm/LH6HK7f0mT8Dl99zCBI/6BMKyVA5
```
その正しく検証ができたJWTのClaimから、flagを取得してください。
(正しく検証できないJWTのClaimから取得できるflagはダミーです。)

## Answer
```
=== VALID JWT line #957 (alg=RS256) ===

header: {"alg": "RS256", "typ": "JWT"}

claims: {

  "flag": "f1nat3xthd{f53c73d9-278e-4b2e-af2e-26b10eed5224}"

} 
```