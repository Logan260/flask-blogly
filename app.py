from flask import Flask, render_template, redirect, request
from models import db, User,app

@app.route('/')
def root():
    """This takes you back to the list of users"""
    return redirect ("/users")

@app.route("/users")
def users_order():
    """This page displays all the information on the users"""
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template("index.html", users=users)

@app.route("/users/new", methods =["GET"])
def users_new_form():
    """This takes you to the form to create a new user"""
    return render_template("new.html")

@app.route("/users/new", methods =["POST"])
def users_new():
    new_user = User(
        first_name=request.form["first_name"],
        last_name=request.form["last_name"],
        image_url=request.form["image_url"]
    )
    db.session.add(new_user)
    db.session.commit()
    return redirect("/users")

@app.route("/users/<int:user_id>")
def users_info(user_id):
    """Shows info on a user"""
    user = User.query.get_or_404(user_id)
    return render_template("show.html", user=user)

@app.route("/users/<int:user_id>/edit")
def users_edit(user_id):
    """This will take you to where you can edit a persons profile"""
    user = User.query.get_or_404(user_id)
    return render_template("edit.html", user=user)

@app.route("/users/<int:user_id>/edit", methods=["POST"])
def user_updating(user_id):
    user=User.query.get_or_404(user_id)
    user.first_name=request.form["first_name"]
    user.last_name=request.form["last_name"]
    user.image_url=request.form["image_url"]
    db.session.add(user)
    db.session.commit()
    return redirect("/users")

@app.route("/users/<int:user_id>/delete", methods=["POST"])
def users_delete(user_id):
    user=User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/users")













