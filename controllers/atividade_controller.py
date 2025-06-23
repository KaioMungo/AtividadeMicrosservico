from flask import Blueprint, request, jsonify
from models.atividade_model import addActivity, getActivities, getActivitiesByProfessorId
from errors import ProfessorNotExist, NoActivityRegistered

activity = Blueprint("activity", __name__)

@activity.route('/')
def index():
    return 'API de Atividades funcionando! Adicione "/atividades" para visualizar'

@activity.route("/atividades", methods=["POST"])
def create_activity():
    data = request.json
    try:
        addActivity(data)
        return jsonify(data), 201
    except ProfessorNotExist as err:
        return jsonify({"Error": str(err)}), 404

@activity.route("/atividades", methods=["GET"])
def get_activities():
    return jsonify(getActivities())

@activity.route("/atividades/<int:professor_id>", methods=['GET'])
def get_activities_by_professor_id(professor_id):
    try:
        return jsonify(getActivitiesByProfessorId(professor_id))
    except ProfessorNotExist as err:
        return jsonify({"Error": str(err)}), 404
    except NoActivityRegistered as err:
        return jsonify({"Error": str(err)}), 404