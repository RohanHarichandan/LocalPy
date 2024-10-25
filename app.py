from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code1']
        output = subprocess.check_output(['python', '-c', code])
        return render_template('index.html', code=code, output=output.decode('utf-8'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)