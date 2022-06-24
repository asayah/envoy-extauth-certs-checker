from flask import Flask, request, abort


app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def auth(path):

    if 'x-forwarded-client-cert' in request.headers:
        print('This is the xfcc:')
        print (request.headers['x-forwarded-client-cert'])
        return 'Allowed!'


    abort(403, {'message': 'Missing Client Cert - Please provide CA cert when establishing the connection'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
