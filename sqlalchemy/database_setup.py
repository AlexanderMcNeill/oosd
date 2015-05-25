__author__ = 'alexmcneill'

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.types import Date

Base = declarative_base()

class Member(Base):
    __tablename__ = 'member'
    id = Column(Integer, primary_key=True)
    fist_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

class TeamMember(Base):
    __tablename__ = 'teammember'
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('member.id'))
    member = relationship(Member)
    team_id = Column(Integer, ForeignKey('team.id'))
    team = relationship(Team)

class ScrumMeeting(Base):
    __tablename__ = 'scrummeeting'
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('team.id'))
    team = relationship(Team)
    date = Column(Date, nullable=False)
    comment = Column(String(250), nullable=False)

class MemberScrum(Base):
    __tablename__ = 'memberscrum'
    id = Column(Integer, primary_key=True)
    scrum_id = Column(Integer, ForeignKey('scrummeeting.id'))
    scrum_meeting = relationship(ScrumMeeting)
    member_id = Column(Integer, ForeignKey('member.id'))
    member = relationship(Member)
    obstacles = Column(String(250), nullable=False)

class MemberGoal(Base):
    __tablename__ = 'membergoal'
    id = Column(Integer, primary_key=True)
    member_scrum_id = Column(Integer, ForeignKey('memberscrum.id'))
    member_scrum = relationship(MemberScrum)
    goal_name = Column(String(50), nullable=False)

class ScrumGoal(Base):
    __tablename__ = 'scrumgoal'
    id = Column(Integer, primary_key=True)
    scrum_id = Column(Integer, ForeignKey('scrummeeting.id'))
    scrum_meeting = relationship(ScrumMeeting)
    goal_name = Column(String(50), nullable=False)

engine = create_engine('sqlite:///agile_manager.db')
Base.metadata.create_all(engine)