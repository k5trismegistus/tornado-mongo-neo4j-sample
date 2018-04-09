import os, sys
sys.path.append(os.getcwd())

from bson.objectid import ObjectId

from entities import Post
from .mongo_repository import MongoRepository
from .neo4j_repository import Neo4jRepository


class PostsRepository(MongoRepository, Neo4jRepository):
    collection_name = 'posts'
    node_type = 'Post'

    def __init__(self):
        MongoRepository.__init__(self)
        Neo4jRepository.__init__(self)

    def find_all(self):
        docs = self.collection.find()
        posts = [
            Post(
                id=doc['_id'],
                title=doc.get('title', ''),
                content=doc.get('content', ''),
            ) for doc in docs
        ]
        return posts

    def find_by_id(self, id):
        print(id)
        doc = self.collection.find_one({'_id': ObjectId(id)})
        post = Post(
                    id=doc['_id'],
                    title=doc['title'],
                    content=doc['content'],
                )
        return post

    def create_post(self, params):
        post_id = self.collection.insert_one({
            'title': params.get('title', ''),
            'content': params('content', '')
        }).inserted_id

        post = Post(id=post_id, title=params.get('title', ''), content=params.get('content', ''))
        return post

    def find_related_posts(self, id):
        with self.graph_database.session() as session:
            with session.begin_transaction() as tx:
                for record in tx.run("MATCH (a:)-[:RELATED]->(f) "
                                    "WHERE a.post_id = {id} "
                                    "RETURN f.id", name=name):
                    print(record)
