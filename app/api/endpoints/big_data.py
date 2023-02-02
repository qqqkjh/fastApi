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

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from imblearn.over_sampling import SMOTE

import numpy as np

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.metrics import roc_curve, auc


from sklearn.model_selection import cross_validate,cross_val_score # 교차타당도
from sklearn.pipeline import make_pipeline # 파이프라인 구축
from sklearn.model_selection import learning_curve, validation_curve # 학습곡선, 검증곡선
from sklearn.model_selection import GridSearchCV # 하이퍼파라미터 튜닝




@router.get("/v1/test")
async def test():

    return {"settings": 'now'}
