from enum import Enum
from pydantic import BaseModel,Field


class Difficulty(str, Enum):
    easy = "Easy"
    medium = "Medium"
    hard = "Hard"

class InterviewCreate(BaseModel):
    role:str
    difficulty:Difficulty
    num_questions:int =Field (
        ge=3,
        le=30
    )

class InterviewResponse(BaseModel):
    id: int
    role: str
    difficulty: str
    num_questions: int
    score: int | None = None
    class Config:
        from_attributes = True


class ScoreUpdate(BaseModel):
    score: int = Field(ge=0, le=100)