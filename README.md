# Elasticsearch with flask demo


# Install Elasticsearch
```
curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
sudo apt update
sudo apt install elasticsearch
```

# Setting
```
sudo vim /etc/elasticsearch/elasticsearch.yml
```
```
# ---------------------------------- Network -----------------------------------
#
# Set the bind address to a specific IP (IPv4 or IPv6):
#
network.host: localhost
```
```
sudo systemctl start elasticsearch
or 
sudo service elasticsearch start

sudo systemctl enable elasticsearch
or
sudo service elasticsearch enable
```

# Testing
```
curl -X GET 'http://localhost:9200'
```
Output for example
```
{
  "name" : "LAPTOP-KFEMN1C9",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "uOO15eCbQCif7j4fsdPt6A",
  "version" : {
    "number" : "7.10.0",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "51e9d6f22758d0374a0f3f5c6e8f3a7997850f96",
    "build_date" : "2020-11-09T21:30:33.964949Z",
    "build_snapshot" : false,
    "lucene_version" : "8.7.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```
# Install Elasticsearch-py
```
python -m pip install elasticsearch
```

# Usage (es_test.py)
```
es = Elasticsearch([{'host':'localhost', 'port':9200}])
load2es(es, index_name, data_path)
```

# json array for example
```
[{"key":"Key1", "content":"content1"},
{"key":"Key2", "content":"content2"}
]
```

# Execute with flask
----
```
1. python3 flaskapp.py
2. 127.0.0.1:5000 on browser
```

# reference
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-18-04 <br>
https://elasticsearch-py.readthedocs.io/en/7.10.0/ <br>
https://soarlin.github.io/2016/11/13/elasticsearch-note-operation/#%E5%9F%BA%E6%9C%AC%E6%8C%87%E4%BB%A4 <br>
