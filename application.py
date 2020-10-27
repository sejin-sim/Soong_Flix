from flask import Flask, render_template, request
import sys
import mv_API

application = Flask(__name__)


@application.route('/')
def home():
    return render_template('soongflix_1.html')

@application.route('/start')
def start():
    return render_template('soongflix_check_1.html')


@application.route('/get_value', methods=['POST','GET'])
def get_value():
    if request.method == 'POST':
        data = []
        data.append(request.form.get('Q1'))
        data.append(request.form.get('Q2'))
        data.append(request.form.get('Q3'))
        data.append(request.form.get('Q4'))
        data.append(request.form.get('Q5'))
        data.append(request.form.get('Q6'))
        data.append(request.form.get('Q7'))
        print(data)                         # test 용
        MV = mv_API.get_data(data)
        return render_template('soongflix_result.html', poster = MV)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]))


# html = templates 폴더
# css, js, image = static 폴더