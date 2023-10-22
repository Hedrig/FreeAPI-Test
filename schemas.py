from pydantic import BaseModel
from datetime import datetime

class Question(BaseModel):
    id: int
    answer: str
    question: str
    created_at: datetime
    # Чтобы Pydantic мог читать не только из dict, но и из атрибутов классов
    class Config:
        from_attributes = True
    
class QuestionQuery(BaseModel):
    questions_num: int = 0