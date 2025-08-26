FROM python:3.11-slim

WORKDIR /app
COPY main.py .

RUN pip install flask

ENV APP_VERSION=v1

EXPOSE 80

CMD ["python", "main.py"]
