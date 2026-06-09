from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)
app.secret_key = "your_secret-key"


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "password123":

            session["logged_in"] = True

            return redirect(url_for("dashboard"))

    return render_template("login.html")

def get_articles():
    articles = []

    for filename in os.listdir("articles"):
        if filename.endswith(".json"):

            with open(f"articles/{filename}", "r") as f:
                article = json.load(f)

            articles.append(article)

    return articles


def get_article_by_id(article_id):
    with open(f"articles/{article_id}.json", "r") as f:
        article = json.load(f)

    return article


@app.route("/")
def home():
    articles = get_articles()

    return render_template(
        "home.html",
        articles=articles
    )


@app.route("/article/<int:article_id>")
def article(article_id):
    article = get_article_by_id(article_id)

    return render_template(
        "article.html",
        article=article
    )


@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    articles = get_articles()
    return render_template(
        "dashboard.html",
        articles=articles
    )

@app.route("/test")
def test():
    return "TEST WORKS"

@app.route("/add", methods=["GET", "POST"])
def add_article():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    if request.method == "POST":

        title = request.form["title"]
        content = request.form["content"]
        date = request.form["date"]

        new_id = len(get_articles()) + 1

        article = {
            "id": new_id,
            "title": title,
            "content": content,
            "date": date
        }

        with open(f"articles/{new_id}.json", "w") as f:
            json.dump(article, f, indent=4)

        return redirect(url_for("dashboard"))

    return render_template("add_article.html")


@app.route("/edit/<int:article_id>", methods=["GET", "POST"])
def edit_article(article_id):
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    article = get_article_by_id(article_id)

    if request.method == "POST":

        article["title"] = request.form["title"]
        article["content"] = request.form["content"]
        article["date"] = request.form["date"]

        with open(f"articles/{article_id}.json", "w") as f:
            json.dump(article, f, indent=4)

        return redirect(url_for("dashboard"))

    return render_template(
        "edit_article.html",
        article=article
    )


@app.route("/delete/<int:article_id>")
def delete_article(article_id):
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    os.remove(f"articles/{article_id}.json")

    return redirect(url_for("dashboard"))

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)