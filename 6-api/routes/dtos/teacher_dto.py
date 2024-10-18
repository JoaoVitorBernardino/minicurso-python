from model.teacher import Teacher

class CreateTeacherDto:
    def __init__(self, data):
        self.name = data.get('name')
        self.expertise = data.get('expertise')

        self.validate()
    
    def validate(self):
        if not self.name or not isinstance(self.name, str):
            raise ValueError("O campo 'name' é obrigatório e deve ser uma string.")
        if not self.expertise or not isinstance(self.expertise, str):
            raise ValueError("O campo 'expertise' é obrigatório e deve ser uma string.")
        
    def to_teacher(self):
        return Teacher(name=self.name, expertise=self.expertise)

class UpdateTeacherDto:
    def __init__(self, id, data):
        self.id = id
        self.name = data.get('name')
        self.expertise = data.get('expertise')

        self.validate()

    def validate(self):
        if not self.id or not isinstance(self.id, int):
            raise ValueError("O campo 'id' é obrigatório e deve ser um int.")
        if not self.name or not isinstance(self.name, str):
            raise ValueError("O campo 'name' é obrigatório e deve ser uma string.")
        if not self.expertise or not isinstance(self.expertise, str):
            raise ValueError("O campo 'expertise' é obrigatório e deve ser uma string.")
        
    def to_teacher(self):
        return Teacher(id=self.id, name=self.name, expertise=self.expertise)