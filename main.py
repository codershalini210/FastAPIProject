from fastapi import FastAPI
from routers.studentsRouter  import router as student_router 
from routers.coursesRouter import router as course_router
app = FastAPI()
@app.get("/")
def home():
    return {"msg": "this is main api home "}
app.include_router(student_router)
app.include_router(course_router)