__author__ = 'alexmcneill'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc

from database_setup import Member, Base, MemberScrum, MemberGoal, TeamMember, Team, ScrumGoal, ScrumMeeting

engine = create_engine('sqlite:///agile_manager.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

try:
    new_member = Member(fist_name="Alex", last_name="McNeill", username="alex", password="a")
    new_member = Member(fist_name="Cam", last_name="Scott", username="cam", password="c")
    session.add(new_member)
    session.commit()
except exc.IntegrityError:
    session.rollback()
    print("Already exists")

members = session.query(Member).all()

for i in range(0, len(members)):
    print(members[i].username + " " + members[i].password)