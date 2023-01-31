from typing import Union, List, Any
from fastapi import APIRouter, Cookie, Header, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
import os
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

# 여기서부터 모델관련 모듈

# 파이선 자체 GUI 관련 모듈
from tkinter import *
# 데이터 분석 라이브러리
import pandas as pd
# 불균형 데이터 샘플링 관련 모듈
from imblearn.over_sampling import SMOTE
# 행렬이나 일반적으로 대규모 다차원 배열을 쉽게 처리할 수 있도록 지원하는 라이브러리
import numpy as np


@router.get("/v1/test")
async def test():
    pd.read_csv
    return {"settings": 'now'}
