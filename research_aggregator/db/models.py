# db/models.py
from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Paper(Base):
    __tablename__ = "papers"
    id = Column(String, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    abstract = Column(Text, nullable=False)
    url = Column(Text, nullable=False)
    published = Column(DateTime, nullable=False)
    summary  = Column(Text)   
    keywords = Column(Text)   




