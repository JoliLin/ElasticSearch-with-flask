import json
import os
import sys
from elasticsearch import Elasticsearch

#load json array to es
def load2es(es, index_name, data_path):
    #json array
    data = json.loads(open(data_path).read())

    for i, j in enumerate(data):
        try:
            es.index(index=index_name, id=i, body=j)
        except ValueError:
            print(f'error: {j}' )

def search(es, index_name, query, size=10):
    search_test = es.search(index=index_name, body={'query':{'match':{'title':query}}, 'size':size} )

    for i in search_test['hits']['hits']:
        print(i['_score'])
        print(i['_source']['title'])

es = Elasticsearch([{'host':'localhost', 'port':9200}])

index_name = sys.argv[1]
#load data
#if data is already loaded, it can be ignored
#data_path = sys.argv[2]
#load2es( es, index_name, data_path )

#print indexes
indexes = es.indices.get(index_name)
print(indexes)

#show data size
count_ = es.cat.count(index_name, params={"format": "json"})
print(f"data size:{count_[0]['count']}")

#query
#query = SEARCH_SOMETHING
#search(es, 'news', query)

