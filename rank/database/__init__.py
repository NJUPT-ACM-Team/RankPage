from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

URI = 'mysql+pymysql://username:password@localhost/acmrank?charset=utf8'

engine = create_engine(URI, isolation_level="READ UNCOMMITTED")
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
