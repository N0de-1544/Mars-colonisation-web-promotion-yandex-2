from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)


# @app.route('/<title>')
# @app.route('/index/<title>')
# def front_page(title):
#     return render_template('index.html', title=title)


@app.route('/list_prof/<list>')
def jobs(list):
    return render_template('jobs.html', listtype=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')