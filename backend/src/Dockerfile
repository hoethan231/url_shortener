FROM python:3-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python3", "server.py", "--reload=true", "--db_path=./database.db", "--port=8080", "--host=0.0.0.0"]