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
    > 해당 디렉토리에 설정 파일 추가
- enums
    > 해당 디렉토리에 enum 클래스 추가
- models 
    > 해당 디렉토리에 Base model 기반 클래스 추가
- tests    
  >해당 디렉토리에 테스트 구현



---  