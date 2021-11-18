# -*- coding: utf-8 -*-
import os

import time
from flask import Flask, render_template, send_from_directory, request, jsonify

app = Flask(__name__)

UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['txt'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload/<string:dynasty>')
def upload_test(dynasty):
    if(dynasty not in ['qing', 'tang', 'muzhi']):
        return '<h1>coming soon.....</h1>'
    return render_template('upload_'+dynasty+'.html')

@app.route('/api/v1.0/breaksent/dynasty/<string:dynasty>', methods=['POST'])
def get_tasks(dynasty):
    model = ''
    if dynasty == 'qing': model = 'models-qing-0920'
    elif dynasty == 'tang': model = 'models_tang_best'
    elif dynasty == 'muzhi': model = 'models_muzhi_0209'
    else: return jsonify({"errno": 1000, "errmsg": "dynasty is wrong"})
    # print(model)
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['myfile']
    if f and allowed_file(f.filename):
        fname = f.filename
        ext = fname.rsplit('.', 1)[1]
        unix_time = int(time.time())
        new_filename = str(unix_time) + '.' + ext
        f.save(os.path.join(file_dir, new_filename))
        print("upload/"+new_filename)
        text = ''
        with open("upload/"+new_filename, 'r') as f:
            text = f.read()
        with open("upload/"+new_filename, 'w') as f:
            text = text.replace("□", "a")
            f.write(text)
        # return jsonify({"errno": 1002, "errmsg": "error"})
        command = "python tagger.py --model "+model+" --input upload/"+new_filename+" --output output/"+new_filename
        print(command)
        try:
            print(os.system(command))
            
            text = ''
            with open("output/" + new_filename, 'r') as f:
                text = f.read()
            with open("output/" + new_filename, 'w') as f:
                text = text.replace("a", "□").replace(' ', '')
                f.write(text)
            directory = os.getcwd()
            return send_from_directory(directory, "output/"+new_filename, as_attachment=True)
        except Exception:
            return jsonify({"errno": 1002, "errmsg": "error"})
    else:
        return jsonify({"errno": 1001, "errmsg": "error"})



if __name__ == '__main__':
    app.run(debug=True)
