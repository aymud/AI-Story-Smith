from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from backend.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Models will inherit from this base class so that they have properties to work with our SQL ORM.
Base = declarative_base()

def get_db():
    """
    Provides a database session for each request
    and ensure we don't have multiple sessions open at the same time.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# When the application starts, we create the tables in the database based on the models defined.
def create_tables():
    Base.metadata.create_all(bind=engine)