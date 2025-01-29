from flask import Flask , render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def get_news():
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'OpenAI',
        'from': '2024-12-30',
        'to': '2025-01-05',
        'sortBy': 'popularity',
        'apiKey': 'Your Api Key' # Can create https://newsapi.org/account
    }
    response = requests.get(url, params=params)
    data = response.json()
    articles = data['articles']
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5002)