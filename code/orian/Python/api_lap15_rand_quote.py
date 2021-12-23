import requests
import json     

url='https://favqs.com/api/qotd'
headers={'Authorization':'Token token=855df50978dc9afd6bf86579913c9f8b', "Content-type" : 'application/json'}


quote_request = requests.get(url,headers=headers)

data=json.loads(quote_request.text)
q_quo=data['quote']
q_auth=q_quo['author']
q_body=q_quo['body']
print(f'{q_body} Author: {q_auth}')
