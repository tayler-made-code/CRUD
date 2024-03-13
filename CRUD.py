from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data store
articles = [{"id": 1, "title": "Hello World", "content": "Welcome to Flask!"}]

@app.route('/')
def index():
    return 'Hello World'

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