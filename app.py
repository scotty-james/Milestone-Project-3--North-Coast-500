import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from forms import SignupForm, SigninForm, AddReviewForm, EditReviewForm, DeleteForm
from datetime import date
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/get_posts")
def get_posts():
    posts = mongo.db.posts.find()
    return render_template("posts.html", posts=posts)


# Sign Up Form Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        existing_users = mongo.db.users
        # checks database to see if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register", form=form))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful!")
        return redirect(url_for("get_posts", username=session["user"]))

    return render_template("register.html", form=form)


# Sign in Form Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        if session['logged_in'] is True:
            return redirect(url_for('index', title="Sign In"))

    form = SigninForm()

    if form.validate_on_submit():
        # checks database to see if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # checks hashed password to ensure match with user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("get_posts", username=session["user"]))
            else:
                # in case where password does not match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login", form=form))

        else:
            # in case where username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login", form=form))

    return render_template("login.html", form=form)


# User Sign Out Route
@app.route("/logout")
def logout():
    flash("You have been signed out")
    session.pop("user")
    return redirect(url_for("login"))


# Add Review Route
@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    today_date = date.today()
    current_date = today_date.strftime("%d %b %y")
    form = AddReviewForm(request.form)
    if form.validate_on_submit():
        mongo.db.posts.insert_one({
            "category_name": request.form.get("category_name"),
            "star_rating": request.form.get("star_rating"),
            "post_title": request.form.get("post_title"),
            "post_description": request.form.get("post_description"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"],
            "review_date": current_date
        })
        flash("Review Submitted")
        return redirect(url_for('get_posts', title='New Post Added'))
    return render_template('add_post.html', title='Add Post', form=form)


# Edit Post Route
@app.route('/edit_post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    today_date = date.today()
    current_date = today_date.strftime("%d %b %y")
    post_db = mongo.db.posts.find_one({'_id': ObjectId(post_id)})
    if request.method == 'GET':
        form = EditReviewForm(data=post_db)
        return render_template('edit_post.html', post=post_db, form=form)
    form = EditReviewForm(request.form)
    if form.validate_on_submit():
        post_db = mongo.db.posts
        post_db.update_one({
            '_id': ObjectId(post_id),
        }, {
            '$set': {
                "category_name": request.form.get("category_name"),
                "star_rating": request.form.get("star_rating"),
                "post_title": request.form.get("post_title"),
                "post_description": request.form.get("post_description"),
                "image_url": request.form.get("image_url"),
                "created_by": session["user"],
                "review_date": current_date
            }
        })
        flash("Review Updated")
        return redirect(url_for('get_posts', title='Review Updated'))
    return render_template('edit_post.html', post=post_db, form=form)


# Delete Post Route
@app.route('/delete_post/<post_id>', methods=['GET', 'POST'])
def delete_post(post_id):
    post_db = mongo.db.posts.find_one({'_id': ObjectId(post_id)})
    if request.method == 'GET':
        form = DeleteForm(data=post_db)
        return render_template('delete_post.html', title="Delete post", form=form)
    form = DeleteForm(request.form)
    if form.validate_on_submit():
        posts_db = mongo.db.posts
        posts_db.delete_one({
            '_id': ObjectId(post_id),
        })
        flash("Review Deleted")
        return redirect(url_for('get_posts', title='Review Deleted'))
    return render_template('delete_post.html', title="delete review", form=form)


# Error handler Route
@app.errorhandler(404)
def handle_404(exception):
    return render_template('404.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
