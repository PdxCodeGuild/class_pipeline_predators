import requests
response = requests.get('https://favqs.com/api/qotd', params={'format': 'json'})
data = response.json()
print(data['quote']['author'])


while True:
    keyword = input('enter a keyword to search for quotes: ')
    page = 1
    while True:
        url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
        headers = {'Authorization': 'Token token=83ff6c5e1850ac35856e1869206dd66e'}
        response = requests.get(url, headers = headers, params={'format': 'json'})
        data = response.json()
        a = data['quotes'][0]['id']
        if a != 0:
            result = len(data['quotes'])
            print(f'{result} quotes associated with {keyword} - page {page}')
        elif a == 0:
            print(f'0 quotes associated with {keyword} - page {page}')
        q = input("enter 'next page' or 'done': ")
        if q == "next page":
            page += 1
            continue
        elif q == "done":
            break
    continue


        




