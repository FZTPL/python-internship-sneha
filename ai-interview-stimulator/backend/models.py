from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import DateTime
from datetime import datetime

class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String,nullable=False)
    difficulty = Column(String,nullable=False)
    num_questions=Column(Integer,nullable=False)
    score = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.now)

