from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_tut.database import Base


class User(Base):

    __tablename__ = 'users'  # Add table name

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,nullable=False,index=True,unique=True)
    email = Column(String, nullable=False, index=True, unique=True)
    hashed_password = Column(String, nullable=False)
    profile = relationship("Profile",back_populates="user",uselist=False)
