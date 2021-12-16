import requests
more_quotes = 'yes'
next_page = 'yes'
page = 0
while more_quotes == 'yes':  
    keyword = input('\nEnter keyword to seach for quotes: ')
    while next_page == 'yes':
        page += 1
        url = (f'https://favqs.com/api/quotes?page={page}&filter={keyword}')
        headers = {'Authorization': 'Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxx'}
        try:
            response = requests.get(url, headers = headers) 
        except requests.exceptions.RequestException as e:  
            print(e)

        quotes = response.json()
        q_list =quotes['quotes']

        print(f'\nPage {page}.')
        for key in q_list:
            print(f"\n\"{key['body']}\"")
            print(f"- {key['author']}")
        next_page = input('\nWould you like to see the next page? (yes or no) ')
    next_page = 'yes'
    page = 0
    more_quotes = input('\nWould like to try another word? (yes or no) ')