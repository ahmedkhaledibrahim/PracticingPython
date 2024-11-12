from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy_tut.database import Base


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer,primary_key=True,index=True)
    bio = Column(String(200))
    user_id = Column(Integer,ForeignKey("users.id"))
    user = relationship("User",back_populates="profile")