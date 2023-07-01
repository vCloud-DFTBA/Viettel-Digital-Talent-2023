FROM python:3.9

WORKDIR /app

COPY . .

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=api.py

EXPOSE 5000

# ENV PYTHONPATH "${PYTHONPATH}:/app"
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]