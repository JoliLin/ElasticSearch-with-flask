import json
import os
import sys
from elasticsearch import Elasticsearch

mapping = { "properties":{
            "content":{
            "type": "text",
            "analyzer": "ik_max_word",
            "search_analyzer": "ik_smart"
}}}

#load json array to es
def load2es(es, index_name, data_path):
    #json array
    data = json.loads(open(data_path).read())
    
    for i, j in enumerate(data):
        print(i)
        try:
            j['mapping'] = mapping
            es.index(index=index_name, id=i, body=j)
        except ValueError:
            print(f'ValueError: {j}' )
        except TypeError:
            print(f'TypeError: {j}')

es = Elasticsearch([{'host':'localhost', 'port':9200}])
#list all indices
es.indices.get_alias("*")

index_name = sys.argv[1]

#load data
data_path = sys.argv[2].encode('utf-8')
load2es(es, index_name, data_path)

#print indexes
indexes = es.indices.get(index_name)
print(json.dumps(indexes, indent=4))

#show data size
count_ = es.cat.count(index_name, params={"format": "json"})
print(f"data size:{count_[0]['count']}")
