from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/CPG"
# :5432 cut after localhost
db = SQLAlchemy(app)

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

    reviews = Reviews.query.limit(20).all()

    

    return render_template("home.html", reviews=reviews)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)