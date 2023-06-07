import os
import json
import requests

# for more details: https://hackmd.io/ATo2tvHpTaq-LK_fJ0QP7A?view


api_key = 'ynyFHpfCzAlHJTS9DAAtLRsD8JziZRK7'
csv_file_path = 'small_file3.csv'

url = 'https://api.dune.com/api/v1/table/upload/csv'

with open(csv_file_path) as open_file:
    data = open_file.read()
    
    headers = {'X-Dune-Api-Key': api_key}

    payload = {
        "table_name": "Lending_historical_dataset3",
        "description": "blank",
        "data": str(data)
    }
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    print('Response status code:', response.status_code)
    print('Response content:', response.content)


