from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from aa import nice
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///finans_piromida.db"
db = SQLAlchemy(app)
articles = [("dsadsadsadsad","jjjjjjjjjjjjj"), ("klkklkljklj","nmnmnnm")]
class Andrcoins(db.Model):
    numero = db.Column(db.INTEGER, primary_key=True, nullable=False)
    Name = db.Column(db.String(200), nullable=False)
    balance = db.Column(db.INTEGER, nullable=False)

    def __repr__(self):
        return '<Are %r>' % self.numero


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Andrcoinsowners')
def posts():
    return render_template("coins.html", articles=nice())


@app.route('/Andrinfo')
def Andrinfo():
    return render_template("Andrinfo.html")


if __name__ == "__main__":
    app.run(debug=True)
