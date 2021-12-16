rand_quote = {
    "qotd_date": "2021-12-04T00:00:00.000+00:00",
    "quote": {
        "id": 22520,
        "tags": [
            "food"
        ],
        "url": "https://favqs.com/quotes/samuel-johnson/22520-no-man-will-b-",
        "favorites_count": 0,
        "upvotes_count": 1,
        "downvotes_count": 0,
        "author": "Samuel Johnson",
        "author_permalink": "samuel-johnson",
        "body": "No man will be a sailor who has contrivance enough to get himself into a jail; for being in a ship is being in a jail, with the chance of being drowned... a man in a jail has more room, better food, and commonly better company."
    }
}
print(f"\nQuote: {rand_quote['quote']['body']}")
print(f"\nby {rand_quote['quote']['author']}")