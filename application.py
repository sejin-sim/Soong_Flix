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
        # if len(data)<7: 선택한 갯수가 7보다 적으면 에러 팝업창을 띄워준다.
        #     return
        print(data)
        mv_API.get_data(data)

        return '결과 화면 output' #return render_template('result.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]))


# html = templates 폴더
# css, js, image = static 폴더