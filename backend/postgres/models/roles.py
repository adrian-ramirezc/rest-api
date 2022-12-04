from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Roles(Base):
    __table_name__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
