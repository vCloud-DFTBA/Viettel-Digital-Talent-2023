# First stage: Build dependencies
FROM python:3.9-alpine3.15 as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

# Second stage: Actual image
FROM python:3.9-alpine3.15

WORKDIR /app

COPY --from=builder /root/.local /root/.local

COPY . .

CMD ["python", "unit-test.py"]
