from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173",
                             "supports_credentials": True, 
                             "Access-Control-Allow-Credentials": True}})

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


