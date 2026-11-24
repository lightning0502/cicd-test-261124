# synopsis
간단한 CI/CD 구성을 위한 프로젝트!

# stack
- backend : fastAPI, uvicorn
- frontend : adminLTE (boostrap base, 4.0.0)
- DB, web server 둘 다 없음!

# python 가상 환경 구성
- python -m venv dev
- (dev) 안 뜰 때 ->
    # Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    # .\dev\Scripts\activate                                              

# python 설치
- (dev) > pip install -r requirements.txt

# uvicorn 설치 (--reload는 핫리로드랑 동일한 듯?)
- uvicorn main:app --reload