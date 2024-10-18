from model.Course import Course

class CreateCourseDto: 
    def __init__(self, data):
        self.name = data.get('name')
        self.hours = data.get('hours')
        self.teacher_id = data.get('teacher_id')

        self.validate()
        

    def validate(self):
        if not self.name or not isinstance(self.name, str):
            raise ValueError("O campo 'name' é obrigatório e deve ser uma string.")
        if not self.hours or not isinstance(self.hours, int):
            raise ValueError("O campo 'hours' é obrigatório e deve ser um int.")
        if not self.teacher_id or not isinstance(self.teacher_id, int):
            raise ValueError("O campo 'teacher_id' é obrigatório e deve ser um int.")
    
    def to_teacher(self):
        return Course(name=self.name, hours=self.hours, teacher_id=self.teacher_id)

class UpdateCourseDto:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.hours = data.get('hours')
        self.teacher_id = data.get('teacher_id')

        self.validate()

    def validate(self):
        if not self.id or not isinstance(self.id, int):
            raise ValueError("O campo 'id' é obrigatório e deve ser um int.")
        if not self.name or not isinstance(self.name, str):
            raise ValueError("O campo 'name' é obrigatório e deve ser uma string.")
        if not self.hours or not isinstance(self.hours, int):
            raise ValueError("O campo 'hours' é obrigatório e deve ser um int.")
        if not self.teacher_id or not isinstance(self.teacher_id, int):
            raise ValueError("O campo 'teacher_id' é obrigatório e deve ser um int.")
    
    def to_teacher(self):
        return Course(id=self.id, name=self.name, hours=self.hours, teacher_id=self.teacher_id)