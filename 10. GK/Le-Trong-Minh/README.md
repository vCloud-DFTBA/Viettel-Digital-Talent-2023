# VDT 2023 - Midterm project
## 1. Write a 3-tier web application (2pts)
### 1.1 Write a CRUD web application to execute:

1. Show the list of students participating in the VDT 2023  - Cloud program in the form of a table (0.5pts) ✅
2. Allow to view details/add/delete/update student information(0.5pts) ✅
Requirement: Source code of each service

Used `FastAPI` to write backend because `FastAPI` supports API testing through `SwaggerUI` interface

Dockerfile for each service:


### 1.2 System design with three services: (0.5pts) ✅

○ web: Web interface written in HTML + CSS + Javascript deployed on the web server nginx
- Source: [Frontend Source code here](https://github.com/letrongminh/Viettel-Digital-Talent-2023/tree/dev-midterm/1.%20Containerization/Le-Trong-Minh/frontend)

○ api: RESTful API written in optional programming language (prefer Python), with full functions: list, get, create, update, delete student information records
- Source: [Backend - api Source code here](https://github.com/letrongminh/Viettel-Digital-Talent-2023/blob/dev-midterm/1.%20Containerization/Le-Trong-Minh/backend)

○ db: A SQL or NoSQL database that stores student information (the initialization data of this DB is given by the table in Appendix I.)
- Source: [Database Source code here](https://github.com/letrongminh/Viettel-Digital-Talent-2023/blob/dev-midterm/1.%20Containerization/Le-Trong-Minh/backend/database.py)


### 1.3 Write unit tests for APIs functionality (0.5pts) ✅

The API's unit test file is as follows:
        ```python
        import pytest
        from fastapi.testclient import TestClient
        from main import app
        import logging

        client = TestClient(app)

        @pytest.fixture(scope="module")
        def student_data():
            return {
                "stt": "100",
                "name": "Le Minh",
                "username": "minhle",
                "year_of_birth": "2000",
                "gender": "male",
                "university": "ITMO",
                "major": "CS"
            }

        def test_post_student(student_data):
            response = client.post("/api/v1/students", json=student_data)
            assert response.status_code == 200
            response_data = response.json()
            del response_data['data']['id']
            expected_data = {
                "data": {
                    "stt": 100,
                    "name": "Le Minh",
                    "username": "minhle",
                    "year_of_birth": 2000,
                    "gender": "male",
                    "university": "ITMO",
                    "major": "CS"
                },
                "code": 200,
                "message": "Student added successfully."
            }
            assert response_data == expected_data

        def test_get_all_students():
            response = client.get("/api/v1/students")
            assert response.status_code == 200
            assert response.json() is not None

        def test_get_student_by_id(student_data):
            response1 = client.post("/api/v1/students", json=student_data)
            student_id = response1.json()['data']['id']
            response2 = client.get(f"/api/v1/students/{student_id}")
            assert response2.status_code == 200
            response2_data = response2.json()
            del response2_data['data']['_id']
            expected_data = {
                'data': {
                    "stt": 100,
                    "name": "Le Minh",
                    "username": "minhle",
                    "year_of_birth": 2000,
                    "gender": "male",
                    "university": "ITMO",
                    "major": "CS"
                },
                'code': 200,
                'message': 'Student data retrieved successfully'
            }
            assert response2_data == expected_data

        def test_update_student(student_data):
            response1 = client.post("/api/v1/students", json=student_data)
            student_id = response1.json()['data']['id']
            updated_data = {
                "stt": 100,
                "name": "Le Minh",
                "username": "minhle",
                "year_of_birth": 2000,
                "gender": "male",
                "university": "ITMO",
                "major": "CS"
            }
            response2 = client.put(f"/api/v1/students/{student_id}", json=updated_data)
            assert response2.status_code == 200
            expected_data = {
                "data": f"Student with ID: {student_id} name update is successful",
                "code": 200,
                "message": "Student name updated successfully"
            }
            assert response2.json() == expected_data

        def test_delete_student(student_data):
            response1 = client.post("/api/v1/students", json=student_data)
            student_id = response1.json()['data']['id']
            response2 = client.delete(f"/api/v1/students/{student_id}")
            assert response2.status_code == 200
            expected_data = {
                "data": f"Student with ID: {student_id} removed",
                "code": 200,
                "message": "Student deleted successfully"
            }
            assert response2.json

        ```

### 1.4 * Write unit tests for interface functions, write integration tests ❌

## 2. Deploy web application using DevOps tools & practices (8 points)

1. Containerization (1 pt)
Request:
    - Write Dockerfile to package the above services into container images (0.5pt) ✅
    - Image requirements ensure optimal build time and occupied size, recommend to use the recommended build image tricks (layer-caching, optimized RUN instructions, multi-stage build etc.) (0.5d) ✅
Output:
    - Dockerfile for each service ✅
    - Output build command and docker history information of each image ✅

### Dockerfiles:

`Frontend`:
```
FROM node:18.2.0-alpine
WORKDIR /app
COPY . /app
RUN npm install 
RUN npm run build
CMD ["npm", "start"]

```
`Frontend Logs`:




`Backend`:

```
FROM python:3.9
WORKDIR /code
COPY . /code
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
```

`Backend Logs`:


`Database Logs`:



2. Continuous Integration (1pt)
Request:

- Automatically run unit test when creating PR on main branch (0.5pt) ✅

- Automatically run unit test when push commit to a branch (0.5pt) ✅

Output:

1. CI tool setup file

The CI flow has been set up as follows:
```yaml
name: Build and test unittest

on:
  push:
    branches: [ "*" ]
  pull_request:
    branches: [ "main" ]

env:
  # Use docker.io for Docker Hub if empty
  REGISTRY: docker.io
  # github.repository as <account>/<repo>
  IMAGE_NAME: ${{ github.repository }}

jobs:

  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Build the Docker image
      run: cd 1.\ Containerization/Le-Trong-Minh/ && docker-compose build
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Test the Docker image
        run: cd 1.\ Containerization/Le-Trong-Minh/ && docker-compose up -d db
      
      ## Unitest
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          cd 1.\ Containerization/Le-Trong-Minh/backend/ && pip install -r requirements.txt
          pip install pytest pytest-cov
        
      - name: Test api
        run: |
          cd 1.\ Containerization/Le-Trong-Minh/backend/api/
          pwd
          pytest test_api.py

```    
- Output log of CI stream


    
    ● More demo images




