from flask import render_template
from project import app

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
