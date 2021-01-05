from elasticsearch import Elasticsearch

def query_string(user_string):
    results = es.search(index="movies", body={"query": {"match": {"title":"{}".format(user_string)}}}, size = 1000)
    hits = results['hits']['total']['value']
    print("Got {} Movies:".format(hits))

    try :
        for i in range(hits):
            print(i+1,') ',results['hits']['hits'][i]['_source']['title'])
    except:
        for i in range(1000):
            print(i+1,') ',results['hits']['hits'][i]['_source']['title'])
            
    return
    


es = Elasticsearch()

print('type "//exit" if you want to exit the search')
user_string = input("Which movie do you want? (by title): \n")

while(user_string != '//exit'):
    query_string(user_string)
    print('type "//exit" if you want to exit the search')
    user_string = input("Which movie do you want? (by title): \n")
