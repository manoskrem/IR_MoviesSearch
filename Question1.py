from elasticsearch import helpers,Elasticsearch
import csv

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

with open('./Data/movies.csv',encoding='utf-8') as file :
    reader = csv.DictReader(file)
    helpers.bulk(es,reader,index='movies',doc_type='doc')


