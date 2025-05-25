# app.py
from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form.get('url')
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else 'タイトルなし'
            result = f'ページタイトル: {title}'
        except Exception as e:
            result = f'エラー: {str(e)}'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run()
