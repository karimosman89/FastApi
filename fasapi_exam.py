from fastapi import FastAPI, HTTPException, Depends, status , Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import List
from random import sample
from utlity import read_questions_from_excel, add_new_question_to_excel

api = FastAPI()
security = HTTPBasic()

# User credentials
USERS = {
    "alice": "wonderland",
    "bob": "builder",
    "clementine": "mandarine",
    "admin": "4dm1N"
}

class Question(BaseModel):
    question: str
    subject: str
    correct: List[str]
    use: str
    responseA: str
    responseB: str
    responseC: str
    responseD: str = None
    remark: str = None


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = credentials.username
    password = credentials.password
    if user not in USERS or USERS[user] != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user

@api.post("/login")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    return {"message": "Login successful"}

@api.get("/healthcheck")
def health_check():
    return {"status": "API is functional"}







@api.post("/questions/new")
def create_new_question(question: Question, credentials: HTTPBasicCredentials = Depends(get_current_user)):
    
    success = add_new_question_to_excel(question)
    if success:
        return {"message": "New question added successfully"}
    else:
        return {"message": "Failed to add the new question"}

@api.get("/questions/")
def filter_questions(test_type, categories):
    questions = read_questions_from_excel()  
    if questions is not None:
        
        filtered_questions = questions[(questions['use'] == test_type) & (questions['subject']==(categories))]
        return filtered_questions
    else:
        return None


@api.get("/generate-mcqs/")
def generate_mcqs(test_type: str, categories: str, count: int = Query(..., description="Number of questions (5, 10, or 20)")):
    
    if count not in [5, 10, 20]:
        raise HTTPException(status_code=400, detail="Count must be 5, 10, or 20")

    
    filtered_questions = filter_questions(test_type, categories)
    if filtered_questions is not None and not filtered_questions.empty:
        
        shuffled_questions = filtered_questions.sample(frac=1).head(count).to_dict(orient='records')
        return shuffled_questions
    else:
        return {"message": "No questions found for the specified criteria"}


