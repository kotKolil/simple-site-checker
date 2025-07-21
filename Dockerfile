FROM python:latest

COPY . /app

WORKDIR /app

RUN pip install -r r.txt --no-cache-dir

EXPOSE 8080

CMD ["python", "server.py"]