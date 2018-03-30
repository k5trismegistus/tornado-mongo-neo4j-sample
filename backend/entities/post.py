from .base_entity import BaseEntity

class Post(BaseEntity):
    def __init__(self, *, id='', title='', content=''):
        self.id = id
        self.title = title
        self.content = content

    def serialize(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'content': self.content
        }
