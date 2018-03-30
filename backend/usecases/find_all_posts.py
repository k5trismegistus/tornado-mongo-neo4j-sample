import os, sys
sys.path.append(os.getcwd())

from entities import Post
from repositories import PostsRepository

class FindAllPosts():
    def __init__(self):
        self.posts_repo = PostsRepository()

    def call(self):
        posts = self.posts_repo.find_all()
        return posts
