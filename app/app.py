from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
import etl
import numpy as np

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/CPG"
# :5432 cut after localhost
db = SQLAlchemy(app)

# create engine
engine = create_engine("postgresql://postgres:postgres@localhost/CPG")
# connect to engine
conn = engine.connect()
# use pd read_sql to connect to sample table
data = pd.read_sql("SELECT * FROM eucerin_intensive_lotion",conn) # refactor this: should be part of etl - add engine,conn as inputs

## Consider making model package - for loading help with speed

#db = create_engine("postgresql://postgres:postgres@localhost:5432/CPG")
class Reviews(db.Model):
    __tablename__ ="eucerin_intensive_lotion"

    id = db.Column(db.Integer, primary_key=True)
    profile_name = db.Column(db.Text)
    stars = db.Column(db.String(20))
    title = db.Column(db.Text)
    review_date = db.Column(db.String(100))
    review = db.Column(db.Text)
    helpful = db.Column(db.String(50))
    form = db.Column(db.String(10))
    brand = db.Column(db.String(20))
    sku = db.Column(db.Text)
    url = db.Column(db.Text)


    def __init__(self,profile_name,stars,title,review_date,review,helpful,form,brand,sku,url):
        self.profile_name = profile_name
        self.stars = stars
        self.title = title
        self.review_date = review_date
        self.review = review
        self.helpful = helpful
        self.form = form
        self.brand = brand
        self.sku = sku
        self.url = url
    
    def __repr__(self):
        return 'Brand: {} and rating {}'.format(self.brand, self.stars)
    


@app.route("/")
def display_reviews():
    return render_template("index.html")


@app.route("/emotions")
def emotion():

    # create engine
    engine = create_engine("postgresql://postgres:postgres@localhost/CPG")
    # connect to engine
    conn = engine.connect()
    # use pd read_sql to connect to sample table
    data = pd.read_sql("SELECT * FROM eucerin_intensive_lotion",conn)

    data = etl.etl(data)
    emotions = etl.monthlyEmotionAvg(data)

    return jsonify(emotions)


# @app.route("/ratings")
# def ratings():
#     # clean data
#     d = etl.etl(data)

#     # groupby
#     g = data.groupby('YearMonth')["stars"].mean()

#     # populate dictionary
#     # ===================   
#     ratings = {}
#     ratings["date"] = g.index.tolist()
#     ratings["avg_monthly"] = list(g) # mean rating over time grouped by month
#     ratings["histogram_values"] = np.histogram(data["stars"], bins=[1,2,3,4,5,6])[0].tolist()
#     ratings["histogram_bins"] = np.histogram(data["stars"], bins=[1,2,3,4,5,6])[1].tolist()
#     ratings["most_helpful"] = data.iloc[data["helpful"].argmax(),5]
#     return jsonify(ratings)

@app.route("/ratings")
def ratings():
    # clean data
    d = etl.etl(data)
    # transformation
    gb = etl.gbReview(d) # refactor with better function names e.g. data = load_transform()

    return jsonify(gb)


@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template("404.html"), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)