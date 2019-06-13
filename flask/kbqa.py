#coding=utf-8
import numpy
from flask import Flask
app = Flask(__name__)

import sys
sys.path.append("../KBQA-BERT-Release/")

from kbqa_api import kbqa_api

@app.route('/<question>/')
def kbqa(question):
    answer = kbqa_api(question)
    return answer

@app.route('/favicon.ico')
def favicon():
    return 'OK'
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
