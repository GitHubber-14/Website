from flask import Flask
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from admin import admin
from main import main
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=1)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.register_blueprint(main)
app.register_blueprint(admin, url_prefix="/admin")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


  