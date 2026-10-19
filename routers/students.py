from fastapi import APIRouter
router = APIRouter()

students = [
 {"id": 1, "name": "A", "course": "Python "},
 {"id": 2, "name": "B", "course": "Data Analysis"},
 {"id": 3, "name": "C", "course": "FastAPI"}
]
@router.get("/students")
def getstudents():
    return students

@router.get("/student/{student_id}")
def get_student_by_id(student_id : int):
    s  = "not found"
    for st in students:
        if(st["id"] == student_id):
            s = st 
            break
    return s