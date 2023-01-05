from fastapi import APIRouter
from app.models import Student

router = APIRouter()


@router.get("/user")
def user():
    student = Student(stdNo="20010001")
    student.name = "Tester"
    return {"message": "this user Domain", "studentModel": student}


@router.post("/user")
def user(student: Student):
    return student
