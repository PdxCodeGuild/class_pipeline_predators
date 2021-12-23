import requests
import json



user_req= 'nature' #input('What word would you like to search for in the qoutes? ')
key_w=user_req
# print(key_w)
user_req2= 0 #input('What page do you want to look on?')

n=0
while n in range(1):
    user_req2=(user_req2 +1)
    
    #print(page_req)
    url=(f'https://favqs.com/api/quotes?page={user_req2}&filter={user_req}')
        #print(url)

    headers={'Authorization':'Token token=855df50978dc9afd6bf86579913c9f8b'}
        #print(headers)

    call_data=requests.get(url,headers=headers)
    quote=call_data.json()
        # data=json.loads(call_data.text)
        #print(data)
        # print(quote)
        # quoutes={data:("body,")}
        #print(quoutes)
        #for datatum in data:
        #print(datatum)
    quote_data=quote['quotes']
        # print(quote_data)
for qt in quote_data:
        #       print(qt)
    body=qt['body']
        
    print(body) 
page_forward= input('Next page? ')
if page_forward =='yes':
    user_req2=(user_req2+1)

if page_forward=='no':
    n=2
