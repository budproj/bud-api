FROM python:3.13-slim

WORKDIR /app

ENV PYTHONPATH=/app

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-root

COPY . /app

EXPOSE 8888

CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]