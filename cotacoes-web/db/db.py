import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pathlib import Path

dotenv_path = os.path.join(Path(os.path.dirname(__file__)).parent, '.env')

if os.path.exists(dotenv_path) and os.path.isfile(dotenv_path):
    dotenv = load_dotenv(dotenv_path)

SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL') or 'sqlite:///./quickdo.db'

db_engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
SQLBase = declarative_base()