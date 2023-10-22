from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    answer = Column("answer", String)
    created_at = Column("created_at", DateTime)