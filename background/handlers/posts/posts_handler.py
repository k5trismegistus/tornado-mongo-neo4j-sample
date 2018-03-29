import tornado.web
import tornado.escape

class PostsHandler(tornado.web.RequestHandler):
    def get(self, **params):
        self.write(tornado.escape.json_encode({
            "status": 200
        }))
