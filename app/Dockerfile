  # 베이스 이미지
  FROM python:3.14.0-slim


  # 워킹 디렉토리 지정(컨테이너 특정 경로)
  # WORKDIR /code
  WORKDIR /app


  # 웹개발시, 사용했던 패키지 목록 파일 카피 리스트
  COPY requirements.txt .


  # 패키지 설치
  RUN pip install --no-cache-dir --upgrade -r requirements.txt


  # 전체 파일을 복사하는 듯.
  # COPY ./app /code/app
  # COPY . . + .dockerignore (오류뜨는디 이거 문법 확인해봐야함)
  COPY . .

  # server sun -> docker-compose에서 처리