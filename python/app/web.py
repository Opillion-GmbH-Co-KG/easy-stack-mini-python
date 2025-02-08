import os
import time
from flask import Flask, render_template, request, make_response

app = Flask(__name__, static_folder='static', static_url_path='')

def get_hit_count():
    count = request.cookies.get("hits", "0")
    try:
        count = int(count) + 1
    except ValueError:
        count = 1
    return count

@app.route('/')
def hello():
    count = get_hit_count()
    response = make_response(render_template("index.html", count=count))
    response.set_cookie("hits", str(count), max_age=60*60*24*365)  # 1 Jahr gültig
    return response

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PYTHON_INTERNAL_PORT", 5000)), debug=True)