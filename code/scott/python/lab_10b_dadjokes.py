import requests
more_jokes = 'y'
while more_jokes == 'y':
    keyword = input('\nEnter a keyword for your Dad Joke search: ')
    url = (f'https://icanhazdadjoke.com/search?term={keyword}')
    headers = {'Accept': 'application/json'}
    try:
        response = requests.get(url, headers = headers) 
    except requests.exceptions.RequestException as e:  
        print(e)
    joke = response.json()
    joke_list = joke['results']
# print(joke_list)
    j_count = len(joke_list)
    more_jokes = 'y'
    index = 0
    while more_jokes == 'y' and index < j_count:
        print(f"\n\"{joke_list[index]['joke']}\"")
        more_jokes = input('\nWould your like to see another joke? (y or n) ')
        index += 1
    more_jokes = input(f'\nThat is all the jokes for "{keyword}". Would you like to continue? (y or n) ')
