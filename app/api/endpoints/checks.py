from typing import Union, List, Any

from fastapi import APIRouter, Cookie, Header
from app.models import Student

router = APIRouter();


@router.get("/check-cookie")
async def check_cookie(ads_id: Union[str, None] = Cookie(default=None)):
    return {"ads_id": ads_id}


@router.get("/check-header")
async def check_header(user_agent: Union[str, None] = Header(default=None)):
    """
    헤더 이름과 일치 (언더바 -> 하이픈, 대 소문자 구별 안함) 하는 파라매터를 선언시 헤더 객체에서 주입해줌
    """
    return {"User-Agent": user_agent}


@router.post("/model-student")
async def model_student(student: Student) -> Student:
    return Student(stdNo=student.stdNo + "_999", name=student.stdNo + " add Name")


@router.post("/model-student-list", response_model=List[Any])
async def model_students(student: Union[Student, Any]) -> Any:
    """
        딕셔너리 연습
    """
    student2 = student.copy()
    student2.name = "두번째 학생"
    student2.stdNo = "2"
    student3 = student
    student3.stdNo = "첫번째 와 동일한 세번째?"
    student4 = dict(student.dict(), **{'name': '새로이 선언된 네번째', 'key': 'value', 'stdNo': '4'})
    student5 = student4.copy()
    student5.update({'name': '복사후 업데이트된 다섯번째', 'stdNo': '5'})

    return [
        {**student.dict(), 'name': '첫번째와 합치기', 'stdNo': '0'},
        {**(None or {}), 'name': '빈껍데기 합치기', 'stdNo': '-1'},
        student,
        student2,
        student3,
        student4,
        student5,
    ]
