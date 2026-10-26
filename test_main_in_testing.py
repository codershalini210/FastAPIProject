from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_students():
    response = client.get("/students")   #will send the GET request 
    assert response.status_code == 200
    assert len(response.json()) ==2

def test_get_one_student():
    response= client.get("/students/1")
    assert response.status_code == 200
   
    assert response.json()["id"] == 1
    assert response.json()["name"] == "John"
    assert response.json()["age"] == 20
    
def test_student_not_found():
    response= client.get("/students/100")
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"