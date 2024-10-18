class Teacher:
    def __init__(self, id=None, name=None, expertise=None):
        self.id = id
        self.name = name
        self.expertise = expertise

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'expertise': self.expertise
        }