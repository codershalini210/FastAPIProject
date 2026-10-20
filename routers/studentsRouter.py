from fastapi import APIRouter
from models.studentModel import Student
router = APIRouter()
# s1 =Student(id="101",name="a",)
students = [Student(id="101",name="a",course="IT"),
            Student(id="102",name="b",course="SW dev")
            ]
@router.post("/students")
def create_student(student:Student):
    students.append(student)
    return {
        "message":"Student added successfully",
        "students":students
    }
@router.get("/students")
def getstudents():
    return students

@router.put("/student/{student_id}")
def update_student(student_id:str,student:Student):
    exists = any(st.id == student_id for st in students )
    
    if exists:
        # return "found"
        for index,s in enumerate(students):
            if (s.id ==student_id):
                # student.id = student_id
                students[index]= student
                return {"msg":"Record updated successfully"}
    else:
      return "not found"
@router.delete("/student/{student_id}")
def delete_student(student_id:str):
    exists = any(st.id == student_id for st in students )
    
    if exists:
        # return "found"
        for index,s in enumerate(students):
            if (s.id ==student_id):
                students.pop(index)
                return "Record deleted Successfully"
                
    else:
      return "not found"    
@router.get("/student/{student_id}")
def get_student_by_id(student_id : str):
    s  = "not found"
    for st in students:
        if(st.id == student_id):
            s = st 
            break
    return s