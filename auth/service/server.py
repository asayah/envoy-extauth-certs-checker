from flask import Flask, request, abort
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import urllib.parse
from datetime import *
from cryptography.x509.oid import NameOID

import ssl, socket

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def auth(path):

    if 'x-forwarded-client-cert' in request.headers:
        print('This is the xfcc:')
        print (request.headers['x-forwarded-client-cert'])

        xfcc = request.headers['x-forwarded-client-cert']
        cert = list(list(xfcc.split(";"))[1].split("="))[1]
        
        cert_decoded = x509.load_pem_x509_certificate( urllib.parse.unquote(cert).encode(), default_backend())
        print("certificate=", cert_decoded)


        # Checking if Expired Cert
        if  datetime.now() > cert_decoded.not_valid_after:
            abort(403, {'message': 'Certificate Expired'})

        if cert_decoded.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value == cert_decoded.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value: 
            abort(403, {'message': 'Self Signed Certificate Presented'})

        return 'Allowed!'
        


    abort(403, {'message': 'Missing Client Cert - Please provide CA cert when establishing the connection'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)



