from flask import Flask, render_template, request
import sys

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('soongflix_1.html')

@app.route('/start')
def start():
    return render_template('soongflix_check_1.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]))

    
    
# html = templates 폴더
# css, js, image = static 폴더