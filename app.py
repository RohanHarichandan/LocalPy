from flask import Flask, render_template, request
from utils.code_execution import translate_code, execute_code
from utils.translation_map import translation_map_hindi, translation_map_odia
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # code=""
    output=""
    translated_code=""
    if request.method == 'POST':
        code = request.form['code1']
        language = request.form.get('language')
        action=request.form.get('action')
        if language =='hi': #hindi
            translated_code=translate_code(code,translation_map_hindi)
        elif language== 'od': #odia 
            translated_code=translate_code(code,translation_map_odia)
        # output = subprocess.check_output(['python', '-c', code])
        if action == 'run':
            output=execute_code(code)
        return render_template('index.html', code=code, output=output,translated_code=translated_code)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)