from sqlalchemy import Column, Integer, String, create_engine,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# Create the database tables


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
# Setup logging
logging.basicConfig(level=logging.INFO)

try:
    db = SessionLocal()
    db.execute(text("SELECT 1"))  # Use text() to explicitly declare SQL expression
    logging.info("Database connection established successfully.")
except Exception as e:
    logging.error(f"Database connection error: {str(e)}")
finally:
    db.close()