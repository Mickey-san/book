from flask import Flask, render_template
from numbers_parser import get_grouped_numbers
import os

app = Flask(__name__)

@app.route('/')
def index():
    result = get_grouped_numbers()
    return render_template('index.html', result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # デフォルトで10000（ローカル用）
    app.run(host="0.0.0.0", port=port)
