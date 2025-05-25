from flask import Flask, render_template
from numbers_parser import get_grouped_numbers

app = Flask(__name__)

@app.route('/')
def index():
    result = get_grouped_numbers()
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
