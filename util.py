import codecs
import json

def load_json(path):
    with codecs.open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())

def subclass_format(dic):
    output = ''
    for k in dic.keys():
        output += f'{k} {dic[k]}<br>'

    return output

def search_format( title, content ):
    if len(title) == 0:
        output = 'Not Found'
    else:
        output = '<div class="list-group">'
        for i in zip(title, content):
            output += '<a class="list-group-item"><h4 class="list-group-item-heading">'+i[0]+'</h4><p class="list-group-item-text">'+i[1]+'</p></a>'
        output += '</div>'
    return output
