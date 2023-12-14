from flask import Blueprint, jsonify
from ..baseball_models import Team, db

bp = Blueprint('teams', __name__, url_prefix='/teams')

# Read endpoint for index of all teams in teams table
@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    teams = Team.query.all() # ORM performs SELECT query
    result = []
    for t in teams:
        result.append(t.serialize()) # build list of Teams as dictionaries
    return jsonify(result) # return JSON response

# Read endpoint for info on specific team
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    t = Team.query.get_or_404(id, "Team not found")
    return jsonify(t.serialize())