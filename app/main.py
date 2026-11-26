from fastapi import FastAPI, Request

# 백엔드 서버에서 동적 구현 -> 템플릿(web), LLM 프롬프트 구성 시 엔진 사용(SSR)
from fastapi.templating import Jinja2Templates

# 정적 데이터 처리(CSS, js 등)
from fastapi.staticfiles import StaticFiles


NAME_STATIC = "static"


app = FastAPI()

# 이러한 구조는 flask와 동일함
app.mount(f"/{NAME_STATIC}", StaticFiles(directory=NAME_STATIC), name=NAME_STATIC) # 정적 데이터의 위치 + URL 표기법 설정
templates = Jinja2Templates(directory="templates") # 폴더 이름과 동일 -> 특정 위치 지정

# 라우팅 + 메서드 정의
@app.get("/") # main home
def home(_request : Request):
    print(_request)
    return templates.TemplateResponse(request=_request, name="index.html")

@app.get("/auth/login")
def page_login(_request : Request):
    print(_request)
    return templates.TemplateResponse(request=_request, name="login-v2.html")

