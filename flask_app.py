
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config["DEBUG"] = True
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="dheetiInterns",
    password="Dsqlpass",
    hostname="dheetiInterns.mysql.pythonanywhere-services.com",
    databasename="dheetiInterns$comments",
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

class Feed(db.Model):

    __tablename__ = "feed"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    idno = db.Column(db.String(30))
    email = db.Column(db.String(30))
    phno = db.Column(db.String(30))
    feed = db.Column(db.String(4096))






@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "GET":
        return render_template("main_page.html")
    if request.method == "POST":
        name = request.form['name']
        idno = request.form['idno']
        email = request.form['email']
        phno = request.form['phone']
        feeds = request.form['feed']
        feed = Feed(name= name, idno = idno ,email = email,phno = phno,feed = feeds)
        db.session.add(feed)
        db.session.commit()
        return "Success"

@app.route('/allfeedback', methods = ['GET'])
def feed():

        return render_template('feedbacks.html', feeds =Feed.query.all())

