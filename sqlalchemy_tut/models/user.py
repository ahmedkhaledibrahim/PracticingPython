from sqlalchemy import Column, Integer,String
from sqlalchemy_tut.database import Base


class User(Base):

    __tablename__ = 'users'  # Add table name

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,nullable=False,index=True,unique=True)
    email = Column(String, nullable=False, index=True, unique=True)
    hashed_password = Column(String, nullable=False)