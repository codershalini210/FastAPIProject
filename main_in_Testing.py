from fastapi import FastAPI, HTTPException 
app = FastAPI()
students =[
    {"id":1,"name":"John","age":20},
    {"id":2,"name":"Ron","age":21}
]

@app.get("/students")
def get_students():
    return students 

@app.get("/students/{student_id}")
def get_student(student_id:int):
    for student in students:
        if( student["id"] == student_id):
            return student
    raise HTTPException(status_code=404, detail="Student not found")