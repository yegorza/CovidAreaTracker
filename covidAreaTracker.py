#Test
import json
import urllib.request

import geocoder
import geopy
from turfpy.measurement import boolean_point_in_polygon
from geojson import Point, Polygon, Feature
from geopy.geocoders import Nominatim
from geopy import distance
import pandas as pd 
from ipyleaflet import Map, AntPath, MeasureControl
import ipywidgets



userLimit = input("Please enter the limit of records for your data set: ")
userLocation = input("Enter your area's id (within your limit)")
url = 'https://data.ontario.ca/en/api/3/action/datastore_search?resource_id=ce9f043d-f0d4-40f0-9b96-4c8a83ded3f6&limit='+ userLimit  
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
   responseData = response.read()

userPoint = geocoder.ip('')
print("User Point",userPoint.latlng)

#Link to library: https://geocoder.readthedocs.io/
userPointCheck = Feature(geometry=Point((userPoint.latlng[0],userPoint.latlng[1])))
print("User Point Check",userPointCheck)
polygon = Polygon(
   [
        [
            (43.714918, -79.394262),
            (43.712859, -79.435642),
            (43.689078, -79.429889),
            (43.692187, -79.385602)
        ]
    ]
)
print("Check point inside polygon: ",boolean_point_in_polygon(userPointCheck, polygon))


responseStr = str(responseData, 'utf-8')
responseJson = json.loads(responseStr)
#print("Response: ", responseJson)
print("=====================================")
records = responseJson['result']['records']
for record in records:
   #print("Record: ", record)
   #Print out the health centre status based on user's location
   if(int(userLocation) == record['_id']):
       print("In your current location these are the requirements: ")
       print("Id: ", record['_id'],"Health Unit:", record['Reporting_PHU'],"Status: ", record['Status_PHU'])

