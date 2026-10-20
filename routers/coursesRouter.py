from fastapi import APIRouter
router = APIRouter()
courses = [
    {"cid":"1","title":"Web development"},
    {"cid":"2","title":"software testing"},
    {"cid":"3","title":"Web design"},
    {"cid":"4","title":"data analysis"}
    ]

@router.get("/courses")
def allcourses():
    return courses

@router.get("/course/{course_id}")
def getcourse(course_id:str):    
    course = "not found"
    for c in courses:
        if(c["cid"] == course_id):
            course = c
            break              
    return {"course": course}