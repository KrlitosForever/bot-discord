FROM python:3.11-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml .
COPY requirements.txt .

RUN uv pip install -r requirements.txt

COPY bot ./bot
COPY .env .

CMD ["python", "bot/main.py"]