from fastapi import FastAPI,Depends,HTTPException
from database import engine,get_db
from models import Base, Interview
from schema import InterviewCreate,InterviewResponse,ScoreUpdate
from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "AI Interview Simulator API"
    }

@app.post("/interview")
def create_interview(
    data: InterviewCreate,
    db: Session = Depends(get_db)
):
    new_interview=Interview(
        role=data.role,
        difficulty=data.difficulty.value,
        num_questions=data.num_questions,
    )
    db.add(new_interview)
    db.commit()
    db.refresh(new_interview)
    return {
    "id": new_interview.id,
    "role": new_interview.role,
    "difficulty": new_interview.difficulty,
    "num_questions": new_interview.num_questions,
    "score": new_interview.score
}

@app.get(
    "/interviews",
    response_model=list[InterviewResponse]
)
def get_interviews(
    db: Session = Depends(get_db)
):
    interviews = db.query(Interview).all()
    return interviews


@app.get("/interview/{interview_id}")
def get_interview(
    interview_id: int,
    db: Session = Depends(get_db)
):
    interview = db.query(Interview).filter(
        Interview.id == interview_id
    ).first()

    if interview is None:
        raise HTTPException(
            status_code=404,
            detail="Interview not found"
        )

    return {
        "id": interview.id,
        "role": interview.role,
        "difficulty": interview.difficulty,
        "num_questions": interview.num_questions,
        "score": interview.score
    }

@app.patch("/interview/{interview_id}/score")
def update_score(
    interview_id: int,
    data: ScoreUpdate,
    db: Session = Depends(get_db)
):
    interview = db.query(Interview).filter(
        Interview.id == interview_id
    ).first()

    if interview is None:
        raise HTTPException(
            status_code=404,
            detail="Interview not found"
        )

    interview.score = data.score

    db.commit()
    db.refresh(interview)

    return {
        "message": "Score updated successfully",
        "id": interview.id,
        "score": interview.score
    }

@app.delete("/interview/{interview_id}")
def delete_interview( interview_id :int,db:Session=Depends(get_db),):
    interview=db.query(Interview).filter(interview_id==Interview.id).first()
    if interview is None:
         raise HTTPException(
            status_code=404,
            detail="Interview not found"
        )
    db.delete(interview)
    db.commit()
    return {"message":"interview deleted succefully"}
    