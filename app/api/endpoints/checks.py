import logging
from typing import Union, List, Any

from fastapi import APIRouter, Cookie, Header
from app.models import Student
from app.core.config import settings

import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/check-env")
async def check_cookie(ads_id: Union[str, None] = Cookie(default=None)):
    """
        쿠키 키값과 일치 하는 값 바인딩
    """
    print(settings)
    return {"settings": settings}

@router.get("/check-cookie")
async def check_cookie(ads_id: Union[str, None] = Cookie(default=None)):
    """
        쿠키 키값과 일치 하는 값 바인딩
    """
    return {"ads_id": ads_id}


@router.get("/check-header")
async def check_header(user_agent: Union[str, None] = Header(default=None)):
    logger.info(user_agent)
    """
    헤더 이름과 일치 (언더바 -> 하이픈, 대 소문자 구별 안함) 하는 파라매터를 선언시 헤더 객체에서 주입해줌
    """
    return {"User-Agent": user_agent}


@router.post("/model-student")
async def model_student(student: Student) -> Student:
    """
        1. BaseModel or Body 값을 매개값으로 받는거만 http body 값 바인딩
        2.일반 자료형 변수를 사용하면 url 쿼리 취급
    """
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


@router.get("/check-unset/{item_id}", response_model=Student, response_model_exclude_unset=True)
async def check_unset(item_id: str):
    """
       response_model_exclude_unset=True
        사용시 값이 Null 일경우 출력하지 않는다

       BaseModal 의 dict 함수
        .dict(exclude_none=True) -> none경우 출력 x
        .dict(exclude_unset=True) -> 한번도 바인딩된적 없을 경우 출력 x
    """
    student = Student(stdNo = item_id)
    student.name = None

    return student.dict(exclude_none=True)
