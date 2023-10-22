from fastapi import FastAPI, Depends
import requests
from sqlalchemy.orm import Session

import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/', response_model=schemas.Question)
def get_questions(query: schemas.QuestionQuery, db: Session = Depends(get_db)):
    params = { "count" : query.questions_num }
    response = requests.get("https://jservice.io/api/random", params)
    questions = response.json()
    for question_json in questions:
        question = schemas.Question(**question_json)
        crud.create_question(db, question)
    return questions[-1]

@app.get('/', response_model=list[schemas.Question])
def list_questions(db: Session = Depends(get_db)):
    return crud.get_questions(db)