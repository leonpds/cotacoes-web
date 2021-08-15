from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .db import SQLBase, db_engine


SQLBase.metadata.create_all(bind=db_engine)