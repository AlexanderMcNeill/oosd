__author__ = 'alexmcneill'

import cherrypy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import orm
from sqlalchemy import exc
from sqlalchemy import and_
import datetime
from database_setup import Member, Base, MemberScrum, MemberGoal, TeamMember, Team, ScrumGoal, ScrumMeeting

class Members:

    exposed = True

    def __init__(self):
        self.options = {
            "add_user": self.add_user,
            "join_team": self.join_team
        }
        self.engine = create_engine('sqlite:///agile_manager.db')
        Base.metadata.bind = self.engine

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        user_request = cherrypy.request.json

        response_root = {"user_function_response": {"response_message": '', "response_code": 1}}
        response = response_root["user_function_response"]

        try:
            response_root = self.options[user_request["function"]](user_request)
        except KeyError:
            response["response_message"] = "Invalid function"

        return response_root

    def add_user(self, request_json):

        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        response_root = {"new_user_response": {"response_message": '', "response_code": 1}}
        response = response_root["new_user_response"]

        new_user_data = request_json["new_user_data"]

        try:

            new_member = Member(fist_name=new_user_data["first_name"], last_name=new_user_data["last_name"], username=new_user_data["username"], password=new_user_data["password"])
            session.add(new_member)
            session.commit()
            response["response_code"] = 0
            response["response_message"] = "Successfully added new user"
            response_root["member"] = {"id": new_member.id,
                                       "first_name": new_member.fist_name,
                                       "last_name": new_member.last_name,
                                       "username": new_member.username}
        except exc.IntegrityError:
            session.rollback()
            response["response_message"] = "Failed, username already taken"
        except KeyError:
            response["response_message"] = "Missing input data"

        return response_root

    def join_team(self, request_json):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        response_root = {"new_user_response": {"response_message": '', "response_code": 1}}
        response = response_root["new_user_response"]

        try:

            if session.query(TeamMember.id).filter(TeamMember.member_id == request_json["user_id"],
                                                   TeamMember.team_id == request_json["team_id"]).count() < 1:
                new_team_member = TeamMember(member_id=request_json["user_id"], team_id=request_json["team_id"])
                session.add(new_team_member)
                session.commit()
                response["response_code"] = 0
                response["response_message"] = "Successfully joined the team"
            else:
                response["response_message"] = "Failed, relationship already exists"
        except KeyError:
            response["response_message"] = "Missing input data"

        return response_root

    @cherrypy.tools.json_out()
    def GET(self, user_name=None, password=None):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        response_root = {"member_request_response": {"response_message": '', "response_code": 1}}
        response = response_root["member_request_response"]

        if user_name is not None and password is not None:
            try:
                member = session.query(Member).filter(and_(Member.username == user_name, Member.password == password)).one()
                response["response_code"] = 0
                response["response_message"] = "found user"

                member_teams = session.query(TeamMember).filter(TeamMember.member_id == member.id).all()
                team_list = []

                for i in range(0,len(member_teams)):
                    team_list.append({"team_name": member_teams[i].team.name, "team_id": member_teams[i].team.id})

                response_root["user"] = {"firstName": member.fist_name, "lastName": member.last_name,
                                         "username": member.username, "id": member.id, "teams": team_list}

            except orm.exc.NoResultFound:
                session.rollback()
                response["response_code"] = 1
                response["response_message"] = "Failed, incorrect username or password"
        else:
            response["response_message"] = "Failed, missing input data"

        session.close()
        return response_root

class Teams:
    exposed = True

    def __init__(self):
        pass

    @cherrypy.tools.json_out()
    def POST(self, team_name=None, password=None):
        engine = create_engine('sqlite:///agile_manager.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        response_root = {"new_team_response": {"response_message": '', "response_code": 1}}
        response = response_root["new_team_response"]

        if team_name is not None and password is not None:
            try:
                new_team = Team(name = team_name, password = password)
                session.add(new_team)
                session.commit()
                response["response_code"] = 0
                response["response_message"] = "Successfully added new team"
                response_root["team"] = {"id": new_team.id,
                                         "name": new_team.name
                                         }

            except exc.IntegrityError:
                session.rollback()
                response["response_message"] = "Failed, team name already taken"
        else:
            response["response_message"] = "Failed, missing input data"

        session.close()
        return response_root


    @cherrypy.tools.json_out()
    def GET(self, user_id=None, team_id=None):
        engine = create_engine('sqlite:///agile_manager.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        response_root = {"get_team_response": {"response_message": '', "response_code": 1}}
        response = response_root["get_team_response"]

        if user_id is not None:
            try:
                member_teams = session.query(TeamMember).filter(TeamMember.member_id == user_id).all()
                response["response_code"] = 0
                response["response_message"] = "found user"
                response_root["teams"] = []
                team_names = response_root["teams"]

                for i in range(0,len(member_teams)):
                    response_root["teams"].append(member_teams[i].team.name)

            except orm.exc.NoResultFound:
                session.rollback()
                response["response_code"] = 1
                response["response_message"] = "User isn't in any teams"

        session.close()
        return response_root

class Scrums:
    exposed = True

    def __init__(self):
        self.options = {
            "add_scrum": self.add_scrum,
            "join_scrum": self.join_scrum
        }
        self.engine = create_engine('sqlite:///agile_manager.db')
        Base.metadata.bind = self.engine

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        scrum_request = cherrypy.request.json

        response_root = {"team_function_response": {"response_message": '', "response_code": 1}}
        response = response_root["team_function_response"]

        try:
            response_root = self.options[scrum_request["function"]](scrum_request)
        except KeyError:
            response["response_message"] = "Invalid function"

        return response_root


    @cherrypy.tools.json_out()
    def GET(self):
        pass

    def add_scrum(self, request_json):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        response_root = {"add_scrum_response": {"response_message": '', "response_code": 1}}
        response = response_root["add_scrum_response"]

        try:
            new_scrum_meeting = ScrumMeeting(team_id=request_json["team_id"], comment=request_json["comment"], date=datetime.datetime.now())
            session.add(new_scrum_meeting)
            session.commit()

            goals = request_json["goals"]

            for i in range(0, len(goals)):
                new_member_goal = ScrumGoal(goal_name=goals[i], scrum_id=new_scrum_meeting.id)
                session.add(new_member_goal)

            session.commit()
            response["response_code"] = 0
            response["response_message"] = "Successfully added a new scrum"

        except KeyError:
            response["response_message"] = "Missing input data"

        return response_root

    def join_scrum(self, request_json):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        response_root = {"join_scrum_response": {"response_message": '', "response_code": 1}}
        response = response_root["join_scrum_response"]

        try:

            if session.query(MemberScrum.id).filter(MemberScrum.member_id == request_json["user_id"],
                                                    MemberScrum.scrum_id == request_json["scrum_id"]).count() < 1:
                new_member_scrum = MemberScrum(member_id=request_json["user_id"], scrum_id=request_json["scrum_id"],
                                              obstacles=request_json["obstacles"])
                session.add(new_member_scrum)
                session.commit()

                goals = request_json["goals"]

                for i in range(0, len(goals)):
                    new_member_goal = MemberGoal(goal_name= goals[i], member_scrum_id=new_member_scrum.id)
                    session.add(new_member_goal)

                session.commit()
                response["response_code"] = 0
                response["response_message"] = "Successfully joined the scrum"
            else:
                response["response_message"] = "Failed, member already contributed to this scrum"
        except KeyError:
            response["response_message"] = "Missing input data"

        return response_root


if __name__ == '__main__':
    cherrypy.tree.mount(
        Members(), '/api/members',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.tree.mount(
        Scrums(), '/api/scrums',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.tree.mount(
        Teams(), '/api/teams',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()