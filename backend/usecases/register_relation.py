import os, sys
sys.path.append(os.getcwd())

from entities import Post
from repositories import PostsRepository

class RegisterRelation():
    def __init__(self, params):
        self.params = params

        self.posts_repo = PostsRepository()

    def call(self):
        lid = self.params.get('lid', None)
        rid = self.params.get('rid', None)

        if not (lid and rid):
            return

        self.posts_repo.register_relation(lid, rid)

        return
