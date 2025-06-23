from flask import Flask, render_template
import json

app = Flask(__name__)

def load_books():
    with open("books.json") as f:
        return json.load(f)

@app.route('/')
def index():
    books = load_books()
    return render_template("index.html", books=books)

@app.route('/book/<int:book_id>')
def book_detail(book_id):
    books = load_books()
    book = next((b for b in books if b["id"] == book_id), None)
    return render_template("book_detail.html", book=book)

if __name__ == "__main__":
    app.run(debug=True)
