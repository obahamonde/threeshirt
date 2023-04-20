FROM python:3.7

WORKDIR /app

COPY . .

EXPOSE 8080

RUN pip install -r requirements.txt

CMD ["python", "main.py"]

