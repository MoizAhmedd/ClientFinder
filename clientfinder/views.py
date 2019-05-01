from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpRequest
from googleplaces import GooglePlaces, types, lang
from typing import Dict
from.models import Location
import os

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

def testView(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    response = HttpResponse('Works')
    return response

def testfindClients(wanted_location,keywords,max_radius) -> Dict :
    b = {wanted_location:keywords,max_radius:3}
    c = "Location:{},Max_Radius:{}".format(b[wanted_location],b[max_radius])
    d = [['f'],['fd'],['fds']]
    e = ""
    for nest in d:
        e += nest[0]
    return e

def findClients(wanted_location,keywords,max_radius) -> Dict :
    clients = {}
    API_KEY = os.environ.get('GOOGLE_API_KEY')
    google_places = GooglePlaces(API_KEY)

    query_result = google_places.nearby_search(
            location=wanted_location, keyword=keywords,
            radius=max_radius, types=[types.TYPE_FOOD])

    for place in query_result.places:
        place.get_details()

        if not place.website: #Checks if place does NOT have a website
                clients[place.name] = place.local_phone_number
                #Dict key = place name, val = place number

        # Are there any additional pages of results?
    if query_result.has_next_page_token:
        query_result_next_page = google_places.nearby_search(
                pagetoken=query_result.next_page_token)

    #This returns all locations as the values to locations, and all numbers as the values to numbers
    #I wanted it to return the key value pairs separately
    num_locations = len(clients.keys())

    returning = " We found "  + str(num_locations) + " locations without a website/\nLocations:{} | Phone Numbers:{}".format(clients.keys(),clients.values())



    #for client in clients:
    #    b = "Location:{} | Phone Number:{}".format(client,clients[client])

    return clients


def foundClientsView(request):
    wanted_location = request.GET.get('location')
    keywords = request.GET.get('keywords')
    max_radius = request.GET.get('radius')
    actual_radius = int(max_radius)
    context = findClients(wanted_location,keywords,actual_radius)
    #print(context)
    return render(request,"result.html",{'d':context})