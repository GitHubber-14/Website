from flask import redirect, url_for, render_template, request, session, flash
from flask import Blueprint, render_template
main = Blueprint("main", __name__, static_folder="static", template_folder="templates")
from models import users
from appinit import db
from appinit import bcrypt

@main.route("/")
def homepage():
    
    
    

    if user in session:
        flash(user + "is in the session")
    
    return render_template("index.html", signin = False)

# to pass a variable through to the html file pas si tthough to the page that uses it and then put it in as seen in the html file

#@app.route("/<name>")
#def user1(name1):
    #return render_template("index.html", name1=name1)
    

#@app.route("/admin")
#def admin():
    #return render_template("index.html", name1="Curtis", adminkey = True)
    #return redirect(url_for("user", name="Curtis", adminkey = True))


        
@main.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        password = request.form["password"]
        email = request.form["email"]
        session["user"] = user     
        session["email"] = email
        session["password"] = password
        


        found_user = users.query.filter_by(name=user).first()
        #found_user = users.query.filter_by(name=user).delete() this will delete one latest user
        # to delete all users do 
        # if found_user:
            #user.delete()   remember to do the commit thingy idek
        
        if found_user:
            flash("Username Already Taken")
            session.pop("user", None)
            session.pop("email", None)
            session.pop("password", None)
            #reject the form 

        #if found_user.email:
            #flash("This email is already in use")

        else:
            #hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            usr = users(user, email, password)
            db.session.add(usr)
            db.session.commit()
            
            return redirect(url_for("main.user"))
    
    return render_template("register.html")

@main.route("/login", methods=["POST", "GET"])   
def login():
    if request.method == "POST":
        session.pop("user", None)
        session.permanent = True
        user = request.form["nm"]
        password = request.form["password"]

        
        #flash("Logged in succesfully")
        #return redirect(url_for("user"))
    #else:
        #if "user" in session:
            #flash("Welcome back.") 
            #return redirect(url_for("user"))

    return render_template("login.html")

@main.route("/user", methods=["POST", "GET"])
def user():
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Your email has been submitted.")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email)
    else:
        flash("You are not logged in.")
        return redirect(url_for("login"))


#@app.route("/register", methods=["POST", "GET"])
#def register():
    #if request.method == "POST":

@main.route("/logout")
def logout():

    flash("You have been logged out successfully.")
    session.pop("user", None)
    session.pop("email", None)
   
    return redirect(url_for("main.homepage"))



