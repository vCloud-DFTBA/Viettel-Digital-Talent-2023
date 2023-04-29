FROM python:3.9-alpine3.15

WORKDIR /code
# EXPOSE 9091 việc để port ở dockerfile chỉ nhằm mục đích
# định hình ko có chức năng gì đặc biệt nên nên loại bỏ để  giảm số lượng layou 
COPY requirements.txt /code
# --no-cachr-dir 
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code


CMD [ "python","app.py" ]