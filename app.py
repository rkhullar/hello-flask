from flask import Flask, jsonify, request
import os

service_name = os.environ.get('SERVICE_NAME', 'hello world')
service_port = os.environ.get('SERVICE_PORT', 8000)
print(service_name, service_port)

app = Flask(__name__)

allowed_http_methods = ['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']


@app.route('/', methods=allowed_http_methods, defaults={'path': ''})
@app.route('/<path:path>', methods=allowed_http_methods)
def catch_all(path):
    return jsonify(service_name=service_name, service_port=service_port, path=f'/{path}', method=request.method)


app.run(host='0.0.0.0', port=service_port)
