from googleplaces import GooglePlaces, types, lang
from typing import Dict
import os

def findClients(wanted_location,keywords,max_radius) -> Dict :
    clients = {}
    API_KEY = ''
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
