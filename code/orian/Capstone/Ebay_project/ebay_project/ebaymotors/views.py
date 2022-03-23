
from django.shortcuts import render, redirect
from xml.dom.minidom import Document
import ebaysdk
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
import xml.etree.ElementTree as ET
from .models import Motorcycles





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
        search_results=response.reply.searchResult.item
        return render(request, 'pages/home.html', {"search_results":search_results})




    



    
