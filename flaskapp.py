import os
import util
from elasticsearch import Elasticsearch
from flask import Flask, render_template, Response, request, redirect, url_for, send_from_directory, current_app

app = Flask(__name__, template_folder='template')
path = '/home/joli/ftp_184/data_1/news_data/'
es = Elasticsearch([{'host':'localhost', 'port':9200}])
es_count = es.cat.count('news', params={"format":"json"})[0]['count']

@app.route('/')
def index():
    return render_template('index.html')
    #return redirect(url_for('print_info'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST' :
        print(request.form)
        if request.form['input'] != '':
            input_ = request.form['input']

            title, content = util.search(es, 'news', input_)
            search_result = util.search_format(title, content) 

            return render_template('search.html', count=es_count, text=input_, search_result=search_result, show=input_)
    
    return render_template('search.html', count=es_count)

if __name__ == '__main__':
    app.run(debug=True)
