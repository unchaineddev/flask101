from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def main():
    return "<h1>Hello World</h1>"


# Another route 
# @app.route('/hello')
# def hello():
#     return "<h1>Hello World! </h1>"

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return 'You made a GET request'
    elif request.method == 'POST':
        return 'You made a POST request'
    else:
        return "<h1>Hello World! </h1>"

# Route with variable
@app.route('/greet/<name>')
def greet_name(name):
    return f'Hello {name}'


# Dynamic URLS
@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return f'{a} + {b} is {a + b}'


# URL params
@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        # return str(request.args)
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f'{greeting}, {name}'
    else:
        return 'Invalid params'


# Status Codes & Custom Responses
# @app.route('/status_codes')
# def status():
#     return 'status code', 404

# Custom Responses
@app.route('/status_codes')
def status():
    res = make_response('Hello World')
    res.status_code = 202
    res.headers['content-type'] = 'text/plain'
    return res


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)  # debug = True
