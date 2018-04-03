import os, sys
sys.path.append(os.getcwd())

import tornado.web
import tornado.escape

from usecases import (
    FindAllPosts,
    CreatePost,
)

class PostsHandler(tornado.web.RequestHandler):
    def get(self, **params):
        posts = FindAllPosts().call()

        self.write(tornado.escape.json_encode({
            'status': 200,
            'posts': [post.serialize() for post in posts]
        }))

    def post(self, **params):
        params = tornado.escape.json_decode(self.request.body)
        post = CreatePost(params).call()

        self.write(tornado.escape.json_encode({
            'status': 201,
            'post': post.serialize()
        }))
