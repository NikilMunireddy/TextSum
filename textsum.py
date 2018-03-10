from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from flask import Flask,render_template,request

import compute

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('inp.html')

@app.route('/sumarizer',methods=['POST','GET'])
def sumarize():
    k=''
    u=''
    n=''
    try:
        k=request.form['key']
        u=request.form['url']
        n=request.form['num']
        print(k)
    except:
        pass
    
   
    sent=compute.compute_un(u,n)
    return render_template('op.html',sent=sent)

app.run(port=5002)

