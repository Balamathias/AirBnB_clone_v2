from flask import Flask, render_template

from form import RegisterForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'qw223je22k422kkejdBSj2k3kn&82923233ndbsjake9393937372'


@app.route('/', strict_slashes=False)
def home():
    return render_template('home.html', data='Hello HBNB!')


@app.route('/register', strict_slashes=False)
@app.route('/sign-up', strict_slashes=False)
def register():
    form = RegisterForm()
    return render_template('register.html', form=form, title="Register")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)