import os
import pathlib
import sys
p = pathlib.Path(__file__).parent.resolve()
sys.path.insert(0, '{}/..'.format(p))
sys.path.insert(0, '{}/.'.format(p))


from dotenv import load_dotenv
from opensearchpy import OpenSearch

from search_core import Search

load_dotenv(dotenv_path='.env')
load_dotenv()

class Open(Search):
    def __init__(self) :
        host = os.environ['opensearch_host']
        port = int(os.environ['opensearch_port'])
        auth = (os.environ['opensearch_user'], os.environ['opensearch_password'])

        self.client = OpenSearch(hosts=[{'host':host, 'port':port}],
            http_compress=True,  # enables gzip compression for request bodies
            http_auth=auth,
            use_ssl=True,
            verify_certs=True,
            )

if __name__ == '__main__':
    from pprint import pprint
    op = Open()
    #print(op.client.get('item_statistics', '127_2023-03-03'))
    op.delete_index('product_feed')
    #op.save_data('pa_test', '1', {'test':'test'})
    #op.define_mapping('water_joli')
