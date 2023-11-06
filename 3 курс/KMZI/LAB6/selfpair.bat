openssl genpkey -algorithm ED448 -out root_keypair.pem
openssl pkey -in root_keypair.pem -noout –text
openssl req \
-new \
-subj “/CN=Root CA” \
-addext “basicConstraints=critical,CA:TRUE” \
-key root_keypair.pem \
-out root_csr.pem
openssl req -in root_csr.pem -noout –text
openssl x509 \
-req \
-in root_csr.pem \
-copy_extensions copyall \
-key root_keypair.pem \
-days 3650 \
-out root_cert.pem
openssl x509 -in root_cert.pem -noout –text
