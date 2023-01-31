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

  
# 불균형 데이터 샘플링 관련 모듈
from imblearn.over_sampling import SMOTE


# 행렬이나 일반적으로 대규모 다차원 배열을 쉽게 처리할 수 있도록 지원하는 라이브러리
import numpy as np


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
 