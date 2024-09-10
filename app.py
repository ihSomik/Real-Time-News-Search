from flask import Flask, render_template, request, url_for
import requests

app = Flask(__name__)

# Add your News API key here
NEWS_API_KEY = "97c06890353f4a7f967909bf7845a050"


# Function to get news based on search query
def get_news(query, page=1):
    url = (
        f"https://newsapi.org/v2/everything?q={query}&page={page}&apiKey={NEWS_API_KEY}"
    )
    response = requests.get(url)
    return response.json().get("articles", [])


# Function to get top headlines
def get_top_headlines():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    return response.json().get("articles", [])


# Function to get news by category
def get_category_news(category, page=1):
    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&page={page}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    return response.json().get("articles", [])


# Home route with search and top headlines
@app.route("/", methods=["GET", "POST"])
def index():
    news_articles = get_top_headlines()  # Display top headlines by default
    query = None
    page = 1  # Default page is 1
    if request.method == "POST":
        query = request.form["query"]
        news_articles = get_news(query, page)
    return render_template("index.html", articles=news_articles, query=query, page=page)


# Route for category-based news
@app.route("/category/<category>", methods=["GET"])
def category_news(category):
    page = 1  # Default to first page
    news_articles = get_category_news(category, page)
    return render_template(
        "index.html", articles=news_articles, category=category, page=page
    )


# Pagination for search results
@app.route("/search", methods=["GET", "POST"])
def search_news():
    query = request.args.get("query")
    page = int(request.args.get("page", 1))  # Default page is 1
    news_articles = get_news(query, page)
    return render_template("index.html", articles=news_articles, query=query, page=page)


if __name__ == "__main__":
    app.run(debug=True)
