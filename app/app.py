from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
import etl
import emotions
import numpy as np

# instantiate app
app = Flask(__name__)

# config app
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/CPG"

# connect to SQLAlchemy
db = SQLAlchemy(app)

# create engine
engine = create_engine("postgresql://postgres:postgres@localhost/CPG")

## Consider making model package - for loading help with speed

# home route    
@app.route("/")
def display_reviews():
    data, ratings_dict = etl.read_transform()
    max_upvoted_review = ratings_dict["max_upvoted_review"] # return this value to use jinja templating

    return render_template("index.html", max_upvoted_review=max_upvoted_review)


# ratings route - this stores the data used during the API call
@app.route("/ratings")
def ratings():
    data, ratings_dict = etl.read_transform() # will want to eventually pass in table name for queries
    return jsonify(ratings_dict)



@app.route("/emotions")
def emotions():

    # will have to modify this when we add filter funcitonality
    df = pd.read_csv("data/emotion_csv/eucerin_intensive_lotion.csv")
    df_dict = {col:df[col].tolist() for col in df}

    return jsonify(df_dict)



@app.route("/max_helpful_review")
def helpful():
    data,ratings_dict = etl.read_transform()
    return jsonify(ratings_dict["max_upvoted_review"])


@app.route("/about_me")
def about_me():
    return render_template("about_me.html")

@app.route("/algorithms")
def algorithms():
    return render_template("algorithms.html")


# have custom error handler for 404 page
@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template("404.html"), 404




if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)