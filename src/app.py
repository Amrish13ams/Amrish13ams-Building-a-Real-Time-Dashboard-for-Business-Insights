from flask import Flask, render_template
from dashboard.metrics import get_metrics

app = Flask(__name__)

@app.route('/')
def home():
    metrics = get_metrics()
    return render_template('dashboard.html', metrics=metrics)

if __name__ == '__main__':
    app.run(debug=True)
