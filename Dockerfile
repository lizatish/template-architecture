FROM python:3.12-alpine

WORKDIR /opt/src

RUN pip --no-cache-dir install poetry==2.0.1

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-cache
RUN pip install uvicorn["standard"]

COPY src /opt/src

ENV PYTHONPATH="${PYTHONPATH}:/opt/"

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
