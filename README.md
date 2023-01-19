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
