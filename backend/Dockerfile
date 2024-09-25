FROM python:3.12-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential \
      && rm -rf /var/lib/apt/lists/*

RUN pip install "poetry"

COPY pyproject.toml poetry.lock app.py ./
COPY src ./src

RUN poetry config virtualenvs.in-project true && \
    poetry install --only=main --no-root

ENTRYPOINT [ "poetry", "run", "uvicorn", "--host", "0.0.0.0", "--port", "5000", "app:app"]