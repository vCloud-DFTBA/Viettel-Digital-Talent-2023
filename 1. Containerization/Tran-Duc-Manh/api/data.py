import requests
import pandas as pd
import time

headers = {
    "authority": "api.viettelcloud.site",
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryzxu3vew0WUELxK7C",
    # 'cookie': 'SL_G_WPT_TO=vi; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1',
    "origin": "https://api.viettelcloud.site",
    "referer": "https://api.viettelcloud.site/docs",
    "sec-ch-ua": '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48",
}
cookies = {
    "SL_G_WPT_TO": "vi",
    "SL_GWPT_Show_Hide_tmp": "1",
    "SL_wptGlobTipTmp": "1",
}
df = pd.read_csv("attendees.csv", sep=";")
for index, item in df.iterrows():
    data = {
        "name": (None, item[1]),
        "program": (None, "Cloud"),
        "title": (None, item[5]),
        "university": (None, item[4]),
        "year": (None, item[2]),
        "sex": (None, item[3]),
    }
    print(data)
    # response = requests.post('http://localhost:8080/api/v1/add-user', headers=headers, files=files)
    response = requests.post(
        "http://58.186.205.96:8081/api/v1/add-user", files=data
    )
    print(response.json())
