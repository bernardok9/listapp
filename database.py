import sqlalchemy as db
import sqlalchemy.orm as dbo
from sqlalchemy.ext.declarative import declarative_base
from config import config
engine = db.create_engine(config.SQLALCHEMY_DATABASE_URI)
db_session = dbo.scoped_session(dbo.sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=engine)