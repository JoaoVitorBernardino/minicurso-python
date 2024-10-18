from flask import Blueprint, request, jsonify
from database.teachers import create_teacher, find_teachers, find_teacher_by_id, update_teacher, delete_teacher
from routes.dtos.teacher_dto import CreateTeacherDto, UpdateTeacherDto

teacher_bp = Blueprint('teacher', __name__, url_prefix='/api')

@teacher_bp.route('/teachers', methods=['POST'])
def add_teacher_route():
    data = request.get_json()
    
    try:
        teacher_dto = CreateTeacherDto(data)
        teacher = teacher_dto.to_teacher()

        result = create_teacher(teacher.name, teacher.expertise)

        if isinstance(result, int):
            teacher.id = result

        response = {
            'status': 'success',
            'message': 'Teacher successfully added',
            'teacher': {
                'id': teacher.id,
                'name': teacher.name,
                'expertise': teacher.expertise
            }
        }

        return jsonify(response), 201
    except ValueError as ve:
        return jsonify({'status': 'error', 'message': str(ve)}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    
@teacher_bp.route('/teachers', methods=['GET'])
def fetch_teachers_route():
    try:
        teachers = find_teachers()

        teachers_dict = [teacher.to_dict() for teacher in teachers] 

        response = {
            'status': 'success',
            'data': teachers_dict
        }

        return jsonify(response), 200
    except ValueError as ve:
        return jsonify({'status': 'error', 'message': str(ve)}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    
@teacher_bp.route('/teachers/<int:id>', methods=['GET'])
def fetch_teacher_by_id_route(id):
    try:
        teacher = find_teacher_by_id(id)

        response = {
            'status': 'success',
            'data': teacher.to_dict()
        }

        return jsonify(response), 200
    except ValueError as ve:
        return jsonify({'status': 'error', 'message': str(ve)}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    
@teacher_bp.route('/teachers/<int:id>', methods=['PUT'])
def update_teacher_route(id):
    data = request.get_json()

    try:
        teacher_dto = UpdateTeacherDto(id, data)

        existing_teacher = find_teacher_by_id(id)
        if not existing_teacher:
            return jsonify({
                'status': 'error',
                'message': f'Teacher with ID {id} not found'
            }), 404

        updated_teacher = update_teacher(teacher_dto.id, teacher_dto.name, teacher_dto.expertise)

        response = {
            'status': 'success',
            'data': updated_teacher.to_dict()
        }

        if updated_teacher:
            return jsonify(response), 200
        else:
            return jsonify({
                'status': 'error',
                'message': 'Failed to update teacher'
            }), 500
    except ValueError as ve:
        return jsonify({'status': 'error', 'message': str(ve)}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    
@teacher_bp.route('/teachers/<int:id>', methods=['DELETE'])
def delete_teacher_route(id):
    try:
        existing_teacher = find_teacher_by_id(id)
        if not existing_teacher:
            return jsonify({
                'status': 'error',
                'message': f'Teacher with ID {id} not found'
            }), 404

        if delete_teacher(id):
            return jsonify({
                'status': 'success',
                'message': f'Teacher with ID {id} deleted successfully'
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'message': 'Failed to delete user'
            }), 500
    except ValueError as ve:
        return jsonify({'status': 'error', 'message': str(ve)}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400