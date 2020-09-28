from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(password)
        print(email)
        return redirect('home')
    return render_template('login.html')


@app.route('/home', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return redirect('summary')
    return render_template('index.html')


@app.route('/summary', methods=['POST', 'GET'])
def summary():
    if request.method == 'POST':
        return redirect('posts')
    return render_template('summary.html')


@app.route('/posts', methods=['POST', 'GET'])
def posts():
    return render_template('posts.html')


if __name__ == '__main__':
    app.run(debug=True)
