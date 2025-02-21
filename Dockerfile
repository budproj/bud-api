FROM python:3.13-slim as build

WORKDIR /app

ENV PYTHONPATH=/app

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-root

COPY . /app

# Run tests
FROM build as test

RUN poetry run pyright

# Run app
FROM build as run

EXPOSE 8888

RUN python manage.py collectstatic

CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]
