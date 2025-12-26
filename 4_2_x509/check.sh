for f in quiz_certs/*.pem; do
  if openssl verify -CAfile ca.pem "$f" >/dev/null 2>&1; then
    echo "$f"
  fi
done

