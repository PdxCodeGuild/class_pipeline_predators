from ast import Param
from distutils.util import execute
from pickle import GET
from re import search
from turtle import title
from urllib import request
from django.http import HttpRequest
from django.shortcuts import render, redirect
from xml.dom.minidom import Document
import ebaysdk
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
# from ebaysdk.shopping import Connection as Shopping
import xml.etree.ElementTree as ET
from .models import Motorcycles

# create html form on home page
# 
# div get and post request
# get request return home page
# post request keyword from form var include ebay request dic

# def add_keyword(request):
#     if request.method == 'GET': 
#         return render(request, 'pages/home.html')
#     elif request.method == 'POST':
#         searchbar = request.POST['searchbar'],
#         makeid = request.POST['make_id'],
#         modelid = request.POST['model_id'],
#         yearid = request.POST['year_id'] 

#         return redirect('home'),



def home(request):
    if request.method == "GET":
        return render(request, 'pages/home.html')
    elif request.method == "POST":
        api = Connection(config_file='ebaysdk-python/Ebay/ebay.yaml', debug=True, siteid="EBAY-MOTOR")
        makeid = request.POST['make_id']
        modelid = request.POST['model_id']
        yearid = request.POST['year_id'] 
        searchbar = request.POST['searchbar']
        condition = request.POST ['condition']
        ebay_request = {
            'keywords': (searchbar, makeid, modelid, yearid),
            'searchFilter': [
                {'Year':yearid,'Make':makeid,'Model':modelid,}
            ],

            # 'compatibility_filter': {'CompatibiltyFilter': [
            #     {'Year':"1974",'Make':"Honda",'Model':"XL350",}
            # ]},
            'itemFilter': [
            {'name': 'condition', 'value': condition, }
        ],
        'paginationInput': {
            'entriesPerPage': 10,
            'pageNumber': 1,
            'content-type': 'application/json',
        },
        'sortOrder': 'bestMatch',
        'outputSelector':'CategoryHistogram'

        
    }
        response = api.execute('findItemsAdvanced', ebay_request)
        # catResponse = api.execute('GetCategories', ebay_request)
        # cat_results=catResponse.reply
        search_results=response.reply.searchResult.item
        # print(cat_results)
        # compat=response.reply.searchResult.item.compatibility 
        # for item in search_results:
        #     item_Id=item.itemId

        #     HttpRequest.POST http://api.ebay.com/buy/browse/v1/item/v1|{item_Id}|check_compatibility
        #     HttpRequest.headers (api = Connection(config_file='ebaysdk-python/Ebay/ebay.yaml', debug=True, siteid="EBAY-MOTOR"))
        # # compID=search_results.itemId
        # print(compID)
        # for item in response.reply.searchResult.item:
        #     print(f"Title: {item.title}, Price: {item.sellingStatus.currentPrice.value}")
  
        return render(request, 'pages/home.html', {"search_results":search_results})




    


# def home(request):
#     api = Connection(config_file='/ebay.yaml', debug=True, siteid="EBAY-US")
#     request = {
#         'keywords': 'honda motorcycle tire',
#         'itemFilter': [
#             {'name': 'condition', 'value': 'new'}
#         ],
#         'paginationInput': {
#             'entriesPerPage': 10,
#             'pageNumber': 1
#         },
#         'sortOrder': 'PricePlusShippingLowest'
#      }
#     response = api.execute('findItemsByKeywords', request)
#     print(response.reply.searchResult.item)
    
