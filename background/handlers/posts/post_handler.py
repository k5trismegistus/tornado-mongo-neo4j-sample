import tornado.web
import tornado.escape

class PostHandler(tornado.web.RequestHandler):
    def get(self, **params):
        self.write(tornado.escape.json_encode({
            "status": 200
        }))
