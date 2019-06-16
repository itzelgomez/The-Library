from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
import os, cgi

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
form = cgi.FieldStorage()
valor = ''
cadena = ''


class Books(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(50))
    book_author = db.Column(db.String(50))
    book_category_name = db.Column(db.String(50))
    book_publishdate = db.Column(db.String(50))
    book_avalible = db.Column(db.Boolean)
    user_name = db.Column(db.String(50))


class Category(db.Model):
    category_name = db.Column(db.String(50), primary_key=True)
    category_description = db.Column(db.String(50))


class User(db.Model):
    user_name = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(50))


@app.route('/')
def user(name='default'):
    return render_template('index.html')

@app.route('/busqueda', methods=["GET", "POST"])
def busqueda():
    valor = request.args.get('valor')
    encontrados = Books.query.filter_by(book_id = valor).first()
    if (encontrados != None):
        return encontrados.book_name
    else:
        return "Libro no encontrado"


if __name__ == '__main__':
    db.create_all()
    app.run(debug = True, port=8000)
