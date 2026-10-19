from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Welcome to first FAstapi project"}

@app.get("/welcome")
def welcome():
    return {"Msg": "welcome to our Fastapi learning "}

@app.get("/students")
def getstudents():
    students =[
        {"id":"st101","name":"John","age":15},
        {"id":"st102","name":"Ron","age":16},
        {"id":"st103","name":"Maria","age":14},
        {"id":"st104","name":"Tania","age":17}
    ]
    return students

@app.get("/services")
def getservices():
    return {"message": " will show services here "}