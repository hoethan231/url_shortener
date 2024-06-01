FROM python:3-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python3", "server.py", "--reload=true", "--db_path=modules.database.db", "--port=8080", "--host=0.0.0.0"]