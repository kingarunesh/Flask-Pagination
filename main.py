from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)


db.create_all()






@app.route("/")
def home():
    # get all users
    # users = User.query.all()

    page = request.args.get('page')

    if page:
        page = int(page)
    else:
        page = 1
    
    pages = User.query.paginate(page=page, per_page=1)

    return render_template("index.html", pages=pages)







@app.route("/create-user", methods=["GET","POST"])
def create_user():
    if request.method == "POST":
        username = request.form["username"]

        new_user = User(username=username)

        db.session.add(new_user)
        db.session.commit()

        # return redirect(url_for("home"))

    return render_template("create-user.html")






if __name__ == "__main__":
    app.run(debug=True)
