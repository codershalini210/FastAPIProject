import os
from dotenv import load_dotenv 
from fastapi import FastAPI,Header,HTTPException
from pydantic import BaseModel
load_dotenv()

app = FastAPI()

STUDENT_TOKEN = os.getenv("STUDENT_TOKEN")

TEACHER_TOKEN = os.getenv("TEACHER_TOKEN")

class Course(BaseModel):
    title:str
    
courses = [
    {"id":1,"title":"Python","Duration ":"3 months"},
    {"id":2,"title":"Data Analysis","Duration ":"2 months"},
    {"id":3,"title":"Data mining","Duration ":"2 months"},
]

def get_role(authorization:str | None):
    if authorization ==f"Bearer {STUDENT_TOKEN}":
        return "student"
    if authorization ==f"Bearer {TEACHER_TOKEN}":
        return "teacher"
    raise HTTPException(status_code=401,detail="Invalid toekn ")

@app.get("/courses")
def get_courses(authorization: str | None =Header(default=None)):
    get_role(authorization)
    return courses

@app.post("/courses")
def add_course(course:Course, authorization: str | None =Header(default=None)):
    role = get_role(authorization)
    if(role != "teacher"):
        raise HTTPException(status_code=403,detail="Only teachers can add courses ")
    new_course = {"id":len(courses)+1,"title":course.title}
    courses.append(new_course)
    return new_course
         