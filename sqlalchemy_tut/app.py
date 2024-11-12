from sqlalchemy.orm import sessionmaker, Session

from sqlalchemy_tut.database import Base, engine, SessionLocal
from sqlalchemy_tut.models import user
from sqlalchemy_tut.models.user import User


session = SessionLocal()

# user_dict ={
#     "username":"ahmed4",
#     "email":"ahmed4@gmail.com",
#     "hashed_password":"12345678"
# }
#
# new_user = User(**user_dict)
#
# session.add(new_user)
# session.commit()
# session.refresh(new_user)

first2users = session.query(User.username).filter(User.id > 1).all()[::-1]
print(first2users)