# import requests
# import pandas as pd
# import time

# df = pd.read_csv("attendees.csv", sep=";")
# for index, item in df.iterrows():
#     data = {
#         #'file':f,
#         #'stt': (None, item[0]),
#         'name': (None, item[1]),
#         'program': (None, 'Cloud'),
#         'title': (None, item[5]),
#         'university': (None, item[4]),
#         'year': (None, item[2]),
#         'sex': (None, item[3]),
#     }
#     print(data)

#     response = requests.post('http://localhost:8080/api/add-user', files=data)
#     print(response.json())