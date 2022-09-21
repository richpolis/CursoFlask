from flask import Flask, request, make_response, redirect, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.remote_addr 
    response = make_response(redirect("/hello"))
    response.set_cookie('user_ip', user_ip)
    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')

    # return f'Hello, World {user_ip}'
    return render_template("hello.html", user_ip=user_ip)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run()

