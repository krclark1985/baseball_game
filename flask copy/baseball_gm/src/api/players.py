from flask import Blueprint, jsonify, abort, request
from ..baseball_models import Player, db


bp = Blueprint('players', __name__, url_prefix='/players')

# Read endpoint for index of all players in players table;
# How to make this so it calls an index of all players on
# a given team?
@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    players = Player.query.all() # ORM performs SELECT query
    result = []
    for p in players:
        result.append(p.serialize()) # build list of Players as dictionaries
    return jsonify(result) # return JSON response

# Read endpoint for specific player in players table
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    p = Player.query.get_or_404(id, "Player not found")
    return jsonify(p.serialize())

# Create endpoint for creating new player to players table
@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'name' not in request.json or 'primary_position' not in request.json:
        return abort(400)
    if 'average' not in request.json or 'rbi' not in request.json or 'homers' not in request.json:
        return abort(400)
    # construct new Player
    p = Player(
        team_id=request.json['team_id'],
        name=request.json['name'],
        primary_position=request.json['primary_position'],
        average=request.json['average'],
        rbi=request.json['rbi'],
        homers=request.json['homers'],
    )
    db.session.add(p) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(p.serialize())

# Delete endpoint for deleting player from players table
@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    p = Player.query.get_or_404(id, "Player not found")
    try:
        db.session.delete(p) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

# Update endpoint for editing info for specific player
@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    p = Player.query.get_or_404(id, 'Player not found')
    if 'name' in request.json:
        return abort(400)
    if 'team_id' in request.json:
        p.team_id = request.json['team_id']
    if 'primary_position' in request.json:
        p.primary_position = request.json['primary_position']
    if 'average' in request.json:
        p.average = request.json['average']
    if 'rbi' in request.json:
        p.rbi = request.json['rbi']
    if 'homers' in request.json:
        p.homers = request.json['homers']
    try:
        db.session.commit()
        return jsonify(p.serialize())
    except:
        return jsonify(False)


    

