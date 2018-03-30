from pymongo import MongoClient
client = MongoClient('mongodb://mongodb')


class MongoRepository():
    collection_name = ''

    def __init__(self):
        database = client['tornado-mongo-neo4j-sample']
        self.collection = database[self.__class__.collection_name]
