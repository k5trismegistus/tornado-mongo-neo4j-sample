import os, sys
sys.path.append(os.getcwd())

import tornado.web
import tornado.escape

class PostHandler(tornado.web.RequestHandler):
    def __init__(self):
        self.post_repo = PostRepository()

    def get(self, **params):
        self.write(tornado.escape.json_encode({
            "status": 200
        }))
