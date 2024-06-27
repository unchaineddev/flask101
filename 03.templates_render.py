from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')


@app.route('/')
def main():
    my_list = ["Bot1", "Bot1", "Bot2", "Bot3", "Bot4", "Bot5"]
    # first_name = 'Unchained'
    # last_name = 'Dev'
    return render_template('index.html', my_list=my_list)


# Using Filters
@app.route('/filter')
def filter():
    some_text = "Hello World"
    return render_template('filter.html', some_text=some_text)


@app.template_filter('rev_string')
def rev_string(s):
    return s[::-1]


@app.template_filter('repeat')
def repeat(s, times=2):
    return s * times


@app.route('/redirect-slug')
def redirect_func():
    return redirect(url_for('filter'))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)  # debug = True