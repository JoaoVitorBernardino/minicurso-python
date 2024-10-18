from flask import Flask, Blueprint
from routes.teacher_routes import teacher_bp

app = Flask(__name__)

app.register_blueprint(teacher_bp)

if __name__ == '__main__':
    app.run(debug=True)