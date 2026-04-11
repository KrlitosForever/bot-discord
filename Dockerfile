FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY requirements.txt .

RUN uv pip install --system -r requirements.txt

COPY bot ./bot

CMD ["python", "-m", "bot.main"]