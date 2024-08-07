import pandas as pd
import requests
import urllib

data = pd.read_csv("WIP_ActualDataSet.csv")
data["Full_PostCode"].fillna("", inplace = True)

apiEndpoint = "http://localhost:8000/postcodes/"

for value in data["Full_PostCode"]:
    if len(value):
        request_url = apiEndpoint + urllib.parse.quote(value)
        query = requests.get(request_url)

        if query.json()['status'] != 200:
            continue

        result = query.json()['result']
        
        parliamentary_constituency = result['parliamentary_constituency']
        admin_county = result['admin_county']


        print(parliamentary_constituency,",", admin_county)
