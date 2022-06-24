# How to Validate Client Certs using extauth

## When Client CA is OK

```bash 
curl https://localhost:8443/hello --key ./configs/security/tls.key --cert ./configs/security/tls.crt -k -i -H 'host: hello.envoyproxy.io'

HTTP/1.1 200 OK
server: envoy
date: Fri, 24 Jun 2022 04:23:28 GMT
content-type: text/html; charset=utf-8
content-length: 11
x-envoy-upstream-service-time: 1

Hello back!%

```


## When Client CA is missing (one way tls):

```
curl  https://localhost:8443/hello -k -H 'host: hello.envoyproxy.io'

<!doctype html>
<html lang=en>
<title>403 Forbidden</title>
<h1>Forbidden</h1>
<p>{&#x27;message&#x27;: &#x27;Missing Client Cert - Please provide CA cert when establishing the connection&#x27;}</p>

```


## WHen CA expired (TBD)




## When CA Self signed (TBD)