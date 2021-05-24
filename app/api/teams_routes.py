from flask import Blueprint, session
from app.models import Team, db
from app.forms import NewTeamForm
from .auth_routes import validation_errors_to_error_messages

teams_routes = Blueprint('teams', __name__)


############################# GET ALL TEAMS #############################
@teams_routes.route('/teams')
def teams():
    teams = Team.query.all()
    return {"teams": [team.to_dict() for team in teams]}

############################ GET ONE TEAM ###############################
@teams_routes.route('/team/<int:id>')
def team(id):
    team = Team.query.get(id)
    return team.to_dict()


########################## POST NEW TEAM ################################
@teams_routes.route('/teams', methods=['POST'])
def new_team():
    form = NewTeamForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        team = Team(
            name=form.data['name'],
            blurb=form.data['blurb'],
            avatar=form.data['avatar'],
            website=form.data['website'],
            github=form.data['github'],
            recruiting=form.data['recruiting'],
        )
        db.session.add(team)
        db.session.commit()
        return team.to_dict()
        # put into utils or imp[ort from auth routes?
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
