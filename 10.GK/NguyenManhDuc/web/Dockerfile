# FROM python:3.9-alpine3.15

# WORKDIR /code
# # EXPOSE 9091 việc để port ở dockerfile chỉ nhằm mục đích
# # định hình ko có chức năng gì đặc biệt nên nên loại bỏ để  giảm số lượng layou 
# COPY requirements.txt /code
# # --no-cachr-dir 
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . /code


# CMD [ "python","app.py" ]

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

CMD ["python", "app.py"]
