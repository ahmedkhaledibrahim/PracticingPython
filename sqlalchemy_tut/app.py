from sqlalchemy.orm import sessionmaker, Session

from sqlalchemy_tut.database import Base, engine, SessionLocal

from sqlalchemy_tut.models.user import User
from sqlalchemy_tut.models.profile import Profile

# Create all tables in the database (this will create tables that are not already created)
Base.metadata.create_all(engine)

session = SessionLocal()
#
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
#
# profile_dict ={
#     "bio":"ahmed4",
#     "user_id":1,
# }
#
# new_profile = Profile(**profile_dict)
#
# session.add(new_profile)
# session.commit()
# session.refresh(new_profile)

firstname = session.query(Profile.bio).join(User.profile).filter(User.id == 1).first()
print(firstname)

firstuser = session.query(User).filter(User.id == 1).first()
print(firstuser.profile.bio)