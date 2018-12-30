#Using Google Places API to find businesses without websites
from googleplaces import GooglePlaces, types, lang

class potclients:
    def __init__(self):
        self.clients = {}

    def addclient(self,newclient,number):
        self.clients[newclient] = number

    def __repr__(self):
        return "{}".format(self.clients)


    def __str__(self):
        print('We found ' +  str(len(self.clients)) + ' location ' + 'without a website')
        return "{}".format(self.clients)
    
    def __len__(self):
        return len(self.clients)

a = potclients()
while len(a) < 10:
    wanted_location = input('What Location are you looking for?')
    keywords = input('What keywords are you looking for?')
    max_radius = int(input('How many meters away are you looking for place?'))


    YOUR_API_KEY = 'AIzaSyB1vilYdjlYwchzO-oW31RS7-6fFK8EpDM'

    google_places = GooglePlaces(YOUR_API_KEY)

        #Finds Places
    query_result = google_places.nearby_search(
            location=wanted_location, keyword=keywords,
            radius=max_radius, types=[types.TYPE_FOOD])


    if query_result.has_attributions:
        print (query_result.html_attributions)


    for place in query_result.places:

        place.get_details()

        if not place.website: #Checks if place does NOT have a website
            a.addclient(place.name,place.local_phone_number)




        # Are there any additional pages of results?
    if query_result.has_next_page_token:
        query_result_next_page = google_places.nearby_search(
                pagetoken=query_result.next_page_token)


    print(a)
