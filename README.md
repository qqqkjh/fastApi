### 파일네이밍룰   
1. 스네이크 케이스로 표현 ex) example_start   
2. 복수형은 끝에 s 붙이기 ex) examples
---
### 디렉토리 구조
```
app
├──api
│  ├─endpoints
│  └─api_collector.py
├──core
├──crud
├──db
├──enums 
├──models
├──schemas
├──tests
├──utils
└──main.py
```
- app
    - api
        - endpoint
            > 해당 디렉토리에 api 구현
        - api_collector.py
            > endpoint api 연결
        - deps.py
            > 디비 세션 연결
- core
    > 해당 디렉토리에 설정 클래스 추가
- crud
    > 각 model의 비즈니스 로직 추가
- db
    > 해당 디렉토리에 DB 커넥터 추가
- enums
    > 해당 디렉토리에 enum 클래스 추가
- models 
    > 해당 디렉토리에 DB 테이블과 일치하는 sqlalchemy 기반 모델 추가
- schemas 
    > 해당 디렉토리에 model 과 연동할 pydantic 기반 BaseModel 추가  
- tests    
    > 해당 디렉토리에 테스트 구현
- utils    
    > 해당 디렉토리에 유틸 관련 클래스 추가
- main.py
    > 시작 모듈



---  
### 로컬 실행방법
사용환경    
- 운영체제 - Window   
- 터미널 - Git Bash
- Python version : 3.9.12
- 로컬가상환경 : pipenv
- IDE : 파이참
```
//app 폴더 상위 루트로 이동 후  
uvicorn app.main:app --port=8000
```

---  
### 필수 환경변수
ENVIRONMENT=<local/dev>   
POSTGRES_SERVER=value   
POSTGRES_USER=value  
POSTGRES_PASSWORD=value   
POSTGRES_DB=value   
POSTGRES_SCHEMA=value

---
### 모델 패키지 관련 목록
```
# 파이선 자체 GUI 관련 모듈
from tkinter import *

# 데이터 분석 라이브러리
import pandas as pd

# 행렬이나 일반적으로 대규모 다차원 배열을 쉽게 처리할 수 있도록 지원하는 라이브러리
import numpy as np

#학습 데이터와 테스트 데이터를 분리해주는 모듈
from sklearn.model_selection import train_test_split

#컬럼마다 다른 변환 설정을 적용하는 모듈
from sklearn.compose import ColumnTransformer

#서로 다른단위를 표준화 해줌 (모든단위를 평균이 0 , 분산은 1로 처리)
from sklearn.preprocessing import StandardScaler

#문장을 숫자로 인코딩하는 기법
from sklearn.preprocessing import OneHotEncoder

# 불균형 데이터 샘플링 관련 모듈
from imblearn.over_sampling import SMOTE

#앙상블 - 여러개의 모델을 묶어 강력한 모델을 만드는 기법
from sklearn.ensemble import GradientBoostingClassifier

#결정트리모델 - 분할과 가지치기로 모델을 생성
from sklearn.tree import DecisionTreeClassifier

# 정오분류표
# confusion_matrix 실제값과 예측한 값간의 오차 행렬
# classification_report - 정밀도, 재현율, F1 값들을 구하고 그 평균값으로 모형의 성능을 평가한다
from sklearn.metrics import confusion_matrix, classification_report

# accuracy_score - 정확도 : 정확히 예측한 수/전체 샘플 수
# precision_score - 정밀도 : 진짜 양성 샘플 수/양성으로 예측된 샘플 수
# recall_score - 재현율 : 양성으로 분류된 샘플 수/전체 양성 샘플 수
# f1_score - 민감도 : 정밀도와 재현율의 조화 평균으로 정밀도와 재현율이 비슷할 수록 F1 score도 높아진다
# roc_auc_score - ROC 곡선 값 계산
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score 

#실제 ROC 곡선을 그리는 모듈
from sklearn.metrics import roc_curve, auc

#클래스를 등록하면 데이터 처리 과정 간 데이터 표준화를 자동으로 해줌
from sklearn.pipeline import make_pipeline

#데이터 교차검증을 통해 데이터 최적화
from sklearn.model_selection import cross_validate,cross_val_score

# 학습곡선, 검증곡선을 통해 데이터 최적화
from sklearn.model_selection import learning_curve, validation_curve

#하이퍼파라미터 값을 학습해 모델 최적화
from sklearn.model_selection import GridSearchCV


```
### 패키지 추가 설명

#### 기본자료구조
> 1. 리스트 [ ] : 리스트
> 2. 튜플 ( ) : 리스트와 거의 동일하나 내부요소 수정불가능
> 3. 딕셔너리 { } : 키-값

#### pandas
[참조사이트](https://wikidocs.net/4367)
> Series
> 1. 1차원 데이터를 다룸 > 배열 오토 인덱싱
> 2. [TestCode](app/tests/test_series.py)

> DataFrame
> 1. 2차원 형식 데이터를 다룸 > 주로 테이블 형식의 데이터
> 2. 컬럼, 데이터(로우), 인덱스로 구성
> 3. 각 요소의 객체는 Series 타입으로 이루어짐
> 4. [TestCode](app/tests/test_dataFrame.py)

#### imblearn
> [SMOTE](https://abluesnake.tistory.com/116#3.%203.%20Over%20Sampling%20-%20SMOTE)   

#### sklearn.preprocessing
> [StandardScaler](https://wpaud16.tistory.com/66)   
> [OneHotEncoder](https://wikidocs.net/22647)   

#### sklearn.ensemble
> [GradientBoostingClassifier](https://wikidocs.net/27577)

#### sklearn.tree
> [DecisionTreeClassifier](https://inuplace.tistory.com/548)

#### sklearn.metrics
> [confusion_matrix](https://m.blog.naver.com/kiddwannabe/221369816719)   
> [classification_report](https://datascienceschool.net/03%20machine%20learning/09.04%20%EB%B6%84%EB%A5%98%20%EC%84%B1%EB%8A%A5%ED%8F%89%EA%B0%80.html)   
> [f1_score](https://for-my-wealthy-life.tistory.com/6)   
> [roc_auc_score](https://for-my-wealthy-life.tistory.com/26)   

#### sklearn.pipeline
> [make_pipeline](https://zephyrus1111.tistory.com/254)

#### sklearn.model_selection
> [train_test_split](https://velog.io/@yuns_u/scikit-learn%EC%9D%98-modelselection-%EB%AA%A8%EB%93%88)   
> [cross_validate, cross_val_score](https://velog.io/@yuns_u/scikit-learn%EC%9D%98-modelselection-%EB%AA%A8%EB%93%88)   
> [learning_curve, validation_curve](https://jellyho.com/blog/85/)    
> [GridSearchCV, 하이퍼파라매터](https://dacon.io/codeshare/4568)   
