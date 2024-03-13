# First create a virtual environment

```bash
python3 -m venv .venv
```

## and activate it

```bash
source .venv/bin/activate
```

# Install Dependencies

```bash
pip3 install flask
```

```bash
pip3 install flask_alchemy
```

## Additionally you can output the dependencies to a text file

```bash
pip3 freeze > requirements.txt
```

Whenever you add a new dependencie you should do this so that anyone working with it can have them

```bash
export FLASK_APP=application.py
export FLASK_ENV=development
```

# Running Flask

```bash
flask run
```

# Showcase CRUD

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data store
articles = [{"id": 1, "title": "Hello World", "content": "Welcome to Flask!"}]

@app.route('/articles', methods=['GET'])
def get_articles():
    return jsonify(articles)

@app.route('/articles', methods=['POST'])
def create_article():
    new_article = request.json
    articles.append(new_article)
    return jsonify(new_article), 201

@app.route('/articles/<int:id>', methods=['PUT'])
def update_article(id):
    article = next((a for a in articles if a['id'] == id), None)
    if article:
        data = request.json
        article.update(data)
        return jsonify(article)
    else:
        return "Article not found", 404

@app.route('/articles/<int:id>', methods=['DELETE'])
def delete_article(id):
    global articles
    articles = [a for a in articles if a['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
```
