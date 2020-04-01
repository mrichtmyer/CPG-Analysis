from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
import etl
import numpy as np

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/CPG"
# :5432 cut after localhost

# connect to SQLAlchemy
db = SQLAlchemy(app)

# create engine
engine = create_engine("postgresql://postgres:postgres@localhost/CPG")

## Consider making model package - for loading help with speed

    
@app.route("/")
def display_reviews():
    return render_template("index.html")


# @app.route("/emotions")
# def emotion():

#     # create engine
#     engine = create_engine("postgresql://postgres:postgres@localhost/CPG")
#     # connect to engine
#     conn = engine.connect()
#     # use pd read_sql to connect to sample table
#     data = pd.read_sql("SELECT * FROM eucerin_intensive_lotion",conn)

#     data = etl.etl(data)
#     emotions = etl.monthlyEmotionAvg(data)

#     return jsonify(emotions)



@app.route("/ratings")
def ratings():
    data, ratings_dict = etl.read_transform() # will want to eventually pass in table name for queries
    return jsonify(ratings_dict)


@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template("404.html"), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)