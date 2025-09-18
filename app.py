from flask import Flask, render_template # type: ignore
import requests  # type: ignore
import os
from dotenv import load_dotenv  # type: ignore

app = Flask(__name__)

API_KEY= os.getenv("NEWSAPI_KEY")
BASE_URL = os.getenv("NEWSAPI_BASE_URL","https://newsapi.org/v2/top-headlines")

@app.route("/")
@app.route("/<category>")
def home(category="general"):
    url= f"{BASE_URL}?country=us&category={category}&apiKey={API_KEY}"
    r=requests.get(url).json()
    news=r.get("articles", [])
    categories = ["general","entertainment","business","health","science","sports","technology"]
    
    
    return render_template('index.html', allNews=news, active_category=category, categories=categories)

if __name__== '__main__':
    app.run(debug=True)