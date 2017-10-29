# generate csr from private key with sha256 hash.
openssl req -new -key my_private_key.key -out my_csr.csr -sha256