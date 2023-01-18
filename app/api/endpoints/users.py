from typing import Union

from fastapi import APIRouter, Query, Path
from app.schemas import Student

router = APIRouter()


@router.get("/user")
def user():
    student = Student(stdNo="20010001")
    student.name = "Tester"
    return {"message": "this user Domain", "studentModel": student}

@router.get("/user-name")
def user_name(name: Union[str, None] = Query(default=None, max_length=3)):
    results = {}
    results.update({"name": name})
    return results

@router.get("/user-rex")
def user_rex(name: Union[str, None] = Query(default=None, max_length=3, regex="^김")):
    results = {}
    results.update({"name": name})
    return results

@router.post("/user")
def user(student: Student = None):
    """
        기본값 을 None 으로 줄경우 넣어도 되고 안 넣어도 되는 파라매터
        기본값이 없는경우 필수값으로 간주한다
    """
    return student


@router.get("/user-path/{user_id}")
def user_path(user_id: str = Path(default=..., max_length=30)):
    results = {}
    results.update({"user_id": user_id})
    return results
