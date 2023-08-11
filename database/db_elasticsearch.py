import datetime
import json
import os 
import pathlib
import sys
from dotenv import load_dotenv
p = pathlib.Path(__file__).parent.resolve().parent
#sys.path.append( f'{p}/')
sys.path.append( f'{p}/database')

from elasticsearch import Elasticsearch 
from search_core import Search

load_dotenv(dotenv_path='.env')
load_dotenv()

class Elastic(Search):
    def __init__(self):
        host = os.environ['host']
        port = int(os.environ['port'])

        host = 'http://localhost' if host == None else host
        port = '9200' if port == None else port

        self.client = Elasticsearch([{'host':host, 'port':port, 'scheme': "http"}])
