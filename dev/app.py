from flask import Flask, request, jsonify
import requests
import ssl
from OpenSSL import crypto

app = Flask(__name__)
def create_ssl_context():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
    return context


if __name__ == '__main__':
    context = create_ssl_context()
    app.run(host='0.0.0.0', port=443, ssl_context=context)
