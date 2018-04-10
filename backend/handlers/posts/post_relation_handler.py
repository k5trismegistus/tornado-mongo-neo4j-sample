import os, sys
sys.path.append(os.getcwd())

import tornado.web
import tornado.escape

from usecases import RegisterRelation

class PostRelationHandler(tornado.web.RequestHandler):
    def post(self, **params):
        id = params['id']
        target_ids = params['target_ids']

        post = RegisterRelation(id, target_ids).call()

        self.write(tornado.escape.json_encode({
            'status': 201,
            'post': post.serialize(),
        }))
