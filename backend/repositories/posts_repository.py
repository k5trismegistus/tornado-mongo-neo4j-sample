import os, sys
sys.path.append(os.getcwd())

from bson.objectid import ObjectId

from entities import Post
from .mongo_repository import MongoRepository


class PostsRepository(MongoRepository):
    collection_name = 'posts'

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
