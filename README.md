# synopsis
간단한 CI/CD 구성을 위한 프로젝트(컨테이너 기반)


# stack
- app
    - backend : fastAPI, uvicorn
    - frontend : boostrap AdminLTE 4.0.0

- DB
    - MySQL

- Proxy
    - nginx

- venv setting
    - Docker (Dockerfile, Docker-compose)


# 개발 환경 구동 명령어
docker-compose up -d --build


# Structure
root:
|   .gitignore
|   docker-compose.yaml
|   README.md
|   
+---.github
|   \---workflows
|           deploy.yaml
|           
+---app
|   |   Dockerfile
|   |   main.py
|   |   requirements.txt
|   |   
|   +---static
|   |   +---assets
|   |   |   \---img
|   |   |       \---credit
|   |   |               
|   |   +---css
|   |   |       
|   |   \---js
|   |           
|   \---templates
|           index.html
|           login-v2.html
|           
+---nginx
|       Dockerfile
|       web.conf