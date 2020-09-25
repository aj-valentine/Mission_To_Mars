# Import dependencies - use Flask to render template, use PyMongo to interact with Mongo database, convert Jupyter notebook to Python
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping

# Set up Flask
app = Flask(__name__)

# Tell Python to connect to Mongo using PyMongo with flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Set up Flask routes - one for main HTML page and one for scraping new data 
# Define route for HTML page: 
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)


# Define route for scraping: 
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"

# Tell Flask to run 
if __name__ == "__main__":
   app.run()