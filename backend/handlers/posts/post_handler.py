import os, sys
sys.path.append(os.getcwd())

import tornado.web
import tornado.escape

from usecases import FindPostById

class PostHandler(tornado.web.RequestHandler):
    def get(self, **params):
        id = params['id']
        post = FindPostById(id).call()

        self.write(tornado.escape.json_encode({
            'status': 200,
            'post': post.serialize(),
        }))
