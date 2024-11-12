import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL


engine = create_engine(DATABASE_URL,echo=True)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = sqlalchemy.orm.declarative_base()



