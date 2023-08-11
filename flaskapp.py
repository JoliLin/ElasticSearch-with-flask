import os
import util
from flask import Flask, render_template, Response, request, redirect, url_for, send_from_directory, current_app

from example import flask_search, get_count

index_name = 'els_test'

app = Flask(__name__, template_folder='template')
es_count = get_count()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST' :
        print(request.form)
        if request.form['input'] != '':
            input_ = request.form['input']

            title, content = flask_search(index_name, input_)
            search_result = util.search_format(title, content) 

            return render_template('search.html', count=es_count, text=input_, search_result=search_result, show=input_)
    
    return render_template('search.html', count=es_count)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
