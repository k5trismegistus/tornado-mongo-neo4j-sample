import tornado.ioloop
import tornado.web
from handlers import (
    PostsHandler,
    PostHandler,
)

def app():
    return tornado.web.Application([
        (r"/api/(?P<version>v\d+)/posts", PostsHandler),
        (r"/api/(?P<version>v\d+)/posts/(?P<id>\d+)", PostHandler),
    ])

if __name__ == "__main__":
    app = app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
