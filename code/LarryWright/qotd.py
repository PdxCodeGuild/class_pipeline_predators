import requests

dictionary = {"qotd_date":"2021-12-04T00:00:00.000+00:00","quote":{"id":44689,"dialogue":False,"private":False,"tags":["nature"],"url":"https://favqs.com/quotes/woody-allen/44689-i-am-two-with-","favorites_count":0,"upvotes_count":1,"downvotes_count":0,"author":"Woody Allen","author_permalink":"woody-allen","body":"I am two with nature."}}

choice = input(' Would you like to see the Quote of the day? yes or no: ')
if choice == ' yes ':
    print(['quote']  ['body'])
elif choice == ' no ':
    print('goodbye!')