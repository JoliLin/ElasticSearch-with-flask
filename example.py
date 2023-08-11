import datetime
import json
import os 
import pathlib
import sys
import fire

p = pathlib.Path(__file__).parent.resolve()
sys.path.append( f'{p}/')

from database.db_elasticsearch import Elastic


index_name = 'els_test'

els = Elastic()

def general_form(query, query_body,  size=10, page=0):
    if query == '':
        result = []
        hits = 0
        es_count = 0
    else:
        result = els.search(index_name, query_body)

        #print(result['hits']['total']['value'])
        #print(result['hits']['hits'][0]['_score'])
        #print(result['hits']['hits'][0]['_source'])

        hits = result['hits']['total']['value']
        es_count = els.client.cat.count(index=index_name, params={"format":
                                                          "json"})[0]['count']
        result = [i['_source'] for i in result['hits']['hits']]
        
    return result

def search(search, size=10, page=0):
    shop_id=142
    
    query_body = {
    'from': size*(page),
    'size': size,
    'query': {
        'multi_match': {
            'query': search,
            'fields': ['name^10', 'description']
            }
        },
        'post_filter':{
            'term': {'shop_id':shop_id}    
        } 
        
    }
    print(query_body)
    
    return general_form(search, query_body, size=size, page=page)


def fitch_by_date(search, size=10, page=0):
    query_body = {
    'from': size*(page),
    'size': size,
    'query':{
        'bool':{
            'filter': [
                        {   
                        "range": {
                            "created_at": {"gte": search}
                        }
                    }
                    ]
            }
        }
    }    
    print(query_body)
    
    return general_form(search, query_body, size=size, page=page)
  
def flask_search(index_name, query, size=10):
    search_ = search(query) 
    
    title = []
    content = []
    
    for i in search_:
        title.append(i['name'])
        try:
            content.append(i['description'])
        except KeyError:
            content.append('')

    return title, content

def get_count():
    return els.get_count(index_name)

def insert_data():
    datapath = '{}/data/test_data.json'.format(p)
    data = json.load(open(datapath))
    for idx, j in enumerate(data):
        els.load2es(idx, j)

if els.client.indices.exists(index=index_name):
    print('### Exist')
    els.status(index_name)
else:
    print('### Initiate')
    els.define_mapping(index_name)


if __name__ == '__main__':
    fire.Fire()
#print(flask_search(index_name, '上衣'))
#print(els.get_count(index_name))
#print(fitch_by_date(els.client, '2020-12-12'))
