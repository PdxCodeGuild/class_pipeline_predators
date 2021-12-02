## Squarespace APIs with PostMan

Practice with GET, POST and DELETE requests using PostMan. 

Objectives:

1. GET request - Find the ID of your current page by retrieving a list of pages through the endpoint **/store_pages**. [Link to documentation](https://developers.squarespace.com/commerce-apis/retrieve-all-store-pages) 

2. POST request - Use the ID of your page to create a product on that page. You can use the following JSON object in the request body. 

```json
{
    "type": "PHYSICAL",
    "storePageId": "add your own page id here",
    "name": "Artisanal Steak Dry Rub",
    "variants": [
        {
            "sku": "SQ0557856",
            "pricing": {
                "basePrice": {
                    "currency": "USD",
                    "value": "12.95"
                }
            }
        }
    ]
}

```
Learn more about creating a product [here](https://developers.squarespace.com/commerce-apis/create-product)

3. DELETE - In order to delete a product on your store, you'll need to [retrieve](https://developers.squarespace.com/commerce-apis/retrieve-all-products) a list of products, grab the ID of the product you want to delete, and use the **/products** endpoint to delete it. Here's how to [delete](https://developers.squarespace.com/commerce-apis/delete-product) a product

3. Before getting started, learn how to make a request using the commerce APIs [here](https://developers.squarespace.com/commerce-apis/making-requests)