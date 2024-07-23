from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), unique=True, index=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(String(60), index=True)

    role = relationship("Role", back_populates="users")
    projects = relationship("Project", back_populates="user")

class Project(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    project_type = Column(String(60), index=True)
    creation_date = Column(String(60), index=True)
    end_date = Column(String(60), index=True)

    user = relationship("User", back_populates="projects")
    client = relationship("Client", back_populates="projects")

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String(60), unique=True, index=True)
    project_type = Column(String(60), index=True)
    creation_date = Column(String(60), index=True)
    end_date = Column(String(60), index=True)

    projects = relationship("Project", back_populates="client")

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(50), index=True)

    users = relationship("User", back_populates="role")
