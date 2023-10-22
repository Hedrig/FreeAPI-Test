from sqlalchemy.orm import Session
import models, schemas


def create_question(db: Session, question: schemas.Question):
    db_question = models.Question(id = question.id,
                                  question = question.question,
                                  answer = question.answer,
                                  created_at = question.created_at)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def get_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Question).offset(skip).limit(limit).all()