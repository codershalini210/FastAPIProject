from fastapi import FastAPI
from models import itemModel
from models.database import Base,engine
from routers.studentsRouter  import router as student_router 
from routers.coursesRouter import router as course_router
from routers.itemsRouter import router as item_router
from routers.ticketsRouter import router as ticket_router

Base.metadata.create_all(bind = engine )
app = FastAPI()
@app.get("/")
def home():
    return {"msg": "this is main api home "}
app.include_router(student_router)
app.include_router(course_router)
app.include_router(item_router)
app.include_router(ticket_router)