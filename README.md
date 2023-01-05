### 파일네이밍룰   
1. 스네이크 케이스로 표현 ex) example_start   
2. 복수형은 끝에 s 붙이기 ex) examples
---
### 디렉토리 구조
```
app
├──api
│  ├─endpoints
│  └─api_router.py
├──core
├──enums 
├──models
└──tests
```
- app
    - api
        - endpoint
            > 해당 디렉토리에 api 구현
        - api_router.py
            > endpoint api 연결
- core
    > 해당 디렉토리에 설정 클래스 추가
- enums
    > 해당 디렉토리에 enum 클래스 추가
- models 
    > 해당 디렉토리에 Base model 기반 클래스 추가
- tests    
  >해당 디렉토리에 테스트 구현



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
sh scripts/start.sh
```
