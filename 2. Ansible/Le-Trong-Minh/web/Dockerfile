FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install --no-cache-dir  --upgrade pip && \
    pip install --no-cache-dir  poetry && \
    poetry config virtualenvs.create false 

ARG DEV=false
RUN if [ "$DEV" = "true" ] ; then poetry install --no-cache --with dev ; else poetry install --no-cache --only main ; fi
COPY ./app/ ./

ENV PYTHONPATH "${PYTHONPATH}:/app"

EXPOSE 8080
CMD uvicorn main:app --host 0.0.0.0 --port 8080
