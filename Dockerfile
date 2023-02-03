#PYTHON BASE IMAGE
FROM python:3.9


WORKDIR /app

#install depedencies
COPY requirements.txt .


RUN pip install -r requirements.txt


COPY . .


CMD ["python", "Halo.py"]