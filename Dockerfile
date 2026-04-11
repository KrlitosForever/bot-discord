FROM python:3.11-slim

WORKDIR /app

RUN pip install uv

COPY requirements.txt .

RUN uv pip install -r requirements.txt

COPY bot ./bot

CMD ["python", "bot/main.py"]