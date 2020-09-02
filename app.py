#######################################################################
# CSS Update : Ctrl + Shift + R
#######################################################################
from flask import Flask, escape, url_for, render_template
from flask import request
from flask import make_response
from datetime import datetime

app = Flask(__name__)

posts = [
    {
        'author': {
            'username': 'test-user 1'
        },
        'title': '첫 번째 포스트',
        'content': '첫 번째 포스트 내용입니다.',
        'date_posted': datetime.strptime('2018-08-01', '%Y-%m-%d')
    },
    {
        'author': {
            'username': 'test-user 2'
        },
        'title': '두 번째 포스트',
        'content': '두 번째 포스트 내용입니다.',
        'date_posted': datetime.strptime('2018-08-02', '%Y-%m-%d')
    }
]

images = [
    {
        'id': 1,
        'title': '첫 번째 포스트',
        'content': '첫 번째 포스트 내용입니다.',
        'source': "https://placeimg.com/640/320/any/1",
        'date': "2020-09-01"
    },
    {
        'id': 2,
        'title': '두 번째 포스트',
        'content': '두 번째 포스트 내용입니다.',
        'source': "https://placeimg.com/640/320/any/2",
        'date': "2020-09-02"
    },
    {
        'id': 3,
        'title': '세 번째 포스트',
        'content': '세 번째 포스트 내용입니다.',
        'source': "https://placeimg.com/640/320/any/3",
        'date': "2020-09-03"
    },
    {
        'id': 4,
        'title': '네 번째 포스트',
        'content': '네 번째 포스트 내용입니다.',
        'source': "https://placeimg.com/640/320/any/4",
        'date': "2020-09-04"
    },
    {
        'id': 5,
        'title': '다섯 번째 포스트',
        'content': '다섯 번째 포스트 내용입니다.',
        'source': "https://placeimg.com/640/320/any/5",
        'date': "2020-09-05"
    }
]


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


# @app.route('/login')
# @app.route('/login/<username>')
# def login(username=None):
#     if username == None:
#         name = request.cookies.get('username')

#         if name == None:
#             resp = make_response(render_template(
#                 'login.html', username="None"))
#             print("User name is {0}.".format("None"))
#         else:
#             resp = make_response(render_template('login.html', username=name))
#             print("User name is {0}.".format(name))

#         return resp
#     else:
#         resp = make_response(render_template('login.html', username=username))

#         resp.set_cookie('username', username)

#         return resp

@app.route("/login", methods=['POST', 'GET'])
def login(email=None):
    email = ""
    password = ""

    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        password = "[" + password + "]"

        print("{0} {1}".format(email, password))

        return render_template("index.html", email=email, password=password)
    else:
        print("Get Request")

        return render_template("login.html", email=email, password=password)


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


@app.route("/carousel")
def carousel():
    return render_template("carousel.html", images=images)


@app.route("/table")
def table():
    return render_template("table.html", images=images)


@app.route("/list")
def list():
    return render_template("list.html")


@app.route("/card")
def card():
    return render_template("card.html", images=images)


@app.route("/form", methods=['POST', 'GET'])
def form():
    inputs = []

    if request.method == "POST":
        email = request.form['exampleInputEmail']
        password = request.form['exampleInputPassword']

        inputs.clear()
        inputs.append(email)
        inputs.append(password)

        print("{0} {1}".format(email, password))
    else:
        print("Get Request")

    return render_template("form.html", title="Form", inputs=inputs)


@app.route("/media")
def media():
    return render_template("media.html", images=images)


@app.route("/navs")
def navs():
    return render_template("navs.html")


@app.route("/scrollspy")
def scrollspy():
    return render_template("scrollspy.html")


@app.route("/collapse")
def collapse():
    return render_template("collapse.html")


@app.route("/pagination")
def pagination():
    return render_template("pagination.html")


@app.route("/jumbotron")
def jumbotron():
    return render_template("jumbotron.html")


@app.route("/breadcrumb")
def breadcrumb():
    return render_template("breadcrumb.html")


@app.route("/button")
def button():
    return render_template("button.html")


@app.route("/dropdowns")
def dropdowns():
    return render_template("dropdowns.html")


@app.route("/progress")
def progress():
    return render_template("progress.html")


@app.route("/spinners")
def spinners():
    return render_template("spinners.html")


@app.route("/badge")
def badge():
    return render_template("badge.html")


@app.route("/alert")
def alert():
    return render_template("alert.html")


@app.route("/toasts")
def toasts():
    return render_template("toasts.html")


@app.route("/tooltips")
def tooltips():
    return render_template("tooltips.html")


@app.route("/popovers")
def popovers():
    return render_template("popovers.html")


@app.route("/modal")
def modal():
    return render_template("modal.html")


@app.route("/utilities")
def utilities():
    return render_template("utilities.html")


if __name__ == '__main__':
    app.run(debug=True)
    #app.run()

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))
