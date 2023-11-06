rem Для создания сертификатов и цепочки сертификации с использованием другого алгоритма в OpenSSL, мы можем вместо алгоритма ED448 использовать, например, алгоритм RSA. Вот изменения, которые нужно внести в ваш код:
rem Генерация корневой пары ключей с алгоритмом RSA:
openssl genpkey -algorithm RSA -out root_keypair.pem
rem Генерация сертификата корневого центра:
openssl req \
-new \
-subj "/CN=Root CA" \
-addext "basicConstraints=critical,CA:TRUE" \
-key root_keypair.pem \
-out root_csr.pem

openssl x509 \
-req \
-in root_csr.pem \
-copy_extensions copyall \
-signkey root_keypair.pem \
-days 3650 \
-out root_cert.pem
rem Генерация промежуточной пары ключей с алгоритмом RSA:
openssl genpkey -algorithm RSA -out intermediate_keypair.pem
rem Генерация сертификата промежуточного центра:
openssl req \
-new \
-subj "/CN=Intermediate CA" \
-addext "basicConstraints=critical,CA:TRUE" \
-key intermediate_keypair.pem \
-out intermediate_csr.pem
openssl x509 \
-req \
-in intermediate_csr.pem \
-copy_extensions copyall \
-CA root_cert.pem \
-CAkey root_keypair.pem \
-days 3650 \
-out intermediate_cert.pem
rem Генерация пары ключей для конечного узла с алгоритмом RSA:
openssl genpkey -algorithm RSA -out leaf_keypair.pem
rem Генерация сертификата для конечного узла:
openssl req \
-new \
-subj "/CN=Leaf" \
-addext "basicConstraints=critical,CA:FALSE" \
-key leaf_keypair.pem \
-out leaf_csr.pem
openssl x509 \
-req \
-in leaf_csr.pem \
-copy_extensions copyall \
-CA intermediate_cert.pem \
-CAkey intermediate_keypair.pem \
-days 3650 \
-out leaf_cert.pem
rem Проверка цепочки сертификации:
openssl verify \
-verbose \
-show_chain \
-trusted root_cert.pem \
-untrusted intermediate_cert.pem \
leaf_cert.pem
rem Эти изменения позволят создать цепочку сертификации с алгоритмом RSA вместо ED448.
rem Важно помнить, что выбор алгоритма зависит от ваших конкретных потребностей
rem и требований безопасности.