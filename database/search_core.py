from abc import abstractmethod
from pprint import pprint


class Search:
    @abstractmethod
    def __init__(self):
        pass

    def define_mapping(self, index_name, setting=dict()):
        '''
        setting = {
            'mappings':{
                'dynamic_templates':[
                        {
                            'float_field': {
                                "match": "CVR",
                                "mapping": {
                                    "type": "float"    
                                    }
                                }

                        },
                        {
                            'float_field': {
                                "match": "CTR",
                                "mapping": {
                                    "type": "float"    
                                    }
                                }

                        }

                    ]
            }
        }
        '''
        if setting:
            self.client.indices.create(index=index_name, body=setting)
        else:
            self.client.indices.create(index=index_name)

    #load json to es
    def save_data(self, index_name, idx, data):
        try:
            self.client.index(index=index_name, id=idx, body=data)
        except ValueError:
            print(f'ValueError')
        except TypeError:
            print(f'TypeError')

    def delete_data_by_id(self, index_name, idx):
        try:
            _ = self.client.delete(index=index_name, id=idx)
            print(_)
        except Exception as e:
            print(e)

    def delete_index(self, index_name):
        try:
            _ = self.client.indices.delete(index=index_name, ignore=[400, 404])
            print(_)
        except Exception as e:
            print(e)

    def status(self, index_name=''):
        if index_name != '':
            print(index_name)
            self.client.indices.refresh(index=index_name)
            pprint(dict(self.client.indices.get(index=index_name)))
            count_ = self.client.cat.count(index=index_name, params={"format": "json"})
            print(f"data size:{count_[0]['count']}")
        else:
            #print indexes
            all_index = self.client.indices.get(index="*")
            ##printable(all_index)
            for i in all_index.keys():
                print(i)

    def get_by_id(self, index_name, idx):
        if self.client.exists(index=index_name, id=idx) == True:
            return self.client.get(index=index_name, id=idx)['_source']
        else:
            return None

    def load2es(self, idx, data):
        try:
            self.client.index(index=index_name, id=idx, body=data)
            print(f'save: {idx}')
        except ValueError:
            print(f'error: {j}' )

    def search(self, index_name, body):
        return self.client.search(index=index_name, body=body)

    def get_count(self, index_name):
        es_count = self.client.cat.count(index=index_name, params={"format":"json"})[0]['count']
        return es_count

