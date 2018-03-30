import os, sys
sys.path.append(os.getcwd())

from entities import Post
from repositories import PostsRepository

class CreatePost():
    def __init__(self, params):
        self.params = params

        self.posts_repo = PostsRepository()

    def call(self):
        params = {
            'title': self.params.get('title', ''),
            'content': self.params.get('content', ''),
        }
        post = self.posts_repo.create_post(params)

        return post
