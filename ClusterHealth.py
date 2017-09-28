import time
import json
import io
import sys
from elasticsearch import Elasticsearch
es = Elasticsearch(['http://elastic:Infowise@localhost:9200'])

class ClusterHealth():
    
    data = es.cluster.health()
    json_Dump_Data = json.dumps(data)
    json_Load_Data = json.loads(json_Dump_Data)
    status = json_Load_Data['status']
    
    active = True

    while active:
        if json_Load_Data.get('status') == 'green':
            goodHealth = 'Your Cluster is green'
            print(goodHealth)
            time.sleep(10)
        elif json_Load_Data.get('status') == 'yellow':
            warning = 'Warning: Your Cluster has turned yellow'
            print(warning)
            time.sleep(10)
        elif json_Load_Data.get('status') == 'red':
            criticalWarning = 'Critical Warning: Your Cluster has turned red!'
            print(criticalWarning)
            time.sleep(10)
