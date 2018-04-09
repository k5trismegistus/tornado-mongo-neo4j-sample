import os, sys
sys.path.append(os.getcwd())

from entities import Post
from repositories import PostsRepository

class FindPostById():
    def __init__(self, id):
        self.id = id
        self.posts_repo = PostsRepository()

    def call(self):
        post = self.posts_repo.find_by_id(self.id)
        related_posts = self.posts_repo.find_related_posts(self.id)

        return post
