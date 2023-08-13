from flask import Flask, render_template, request

app = Flask(__name__)

# Хранилище комментариев в виде списка словарей
comments = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["comment_text"]
        category = request.form["comment_category"]
        comments.append({"text": text, "category": category})
    return render_template("index.html", comments=comments)

if __name__ == "__main__":
    app.run(debug=True)
