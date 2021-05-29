#CovidAreaTracker
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
from shapely.geometry import Point
import healthUnitCoordinateStrings
import datetime

def getPolygonFromStr(geocodesString):
    coordArray = []
    coordinates = geocodesString.split(" ")
    for coordStr in coordinates:
        coord = coordStr.split(",")
        lat = float(coord[1])
        lng = float(coord[0])
        coordArray.append((lat,lng))
    
    
    return Polygon([coordArray])
def convertToReadableDate(dateValue):
    convertedDate = datetime.datetime.strptime(dateValue, '%Y-%m-%dT%H:%M:%S')
    readableDate = datetime.datetime.strftime(convertedDate,'%B %d, %Y')
    return readableDate

def getHealthUnitStatusFromAPI(healthUnitId):
    userLimit = 500
    # userLocation = input("Enter your area's id (within your limit)")
    url = 'https://data.ontario.ca/en/api/3/action/datastore_search?resource_id=ce9f043d-f0d4-40f0-9b96-4c8a83ded3f6&limit='+ str(userLimit)  
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        responseData = response.read()
        responseStr = str(responseData, 'utf-8')
        responseJson = json.loads(responseStr)
        #print("Response: ", responseJson)
        print("=====================================")
        records = responseJson['result']['records']

    #lastStatusRecord = records[len(records)]

    healthUnitRecords = []
    for record in records:
       #print("Record: ", record)
       #Print out the health centre status based on user's location\
       if(record['Reporting_PHU_id'] == healthUnitId):    
            healthUnitRecords.append(record)

    latestHealthUnitRecord = healthUnitRecords[len(healthUnitRecords)-1]
    print("Your Current Location ",userPoint)
    print(" ")
    print("========Identified Information (Ontario Government Database Covid-19 Current Status)=========")
    print("Health Unit:", latestHealthUnitRecord['Reporting_PHU'])
    print("Latest Location Status For Covid-19: ", latestHealthUnitRecord['Status_PHU'])
    print("Start Date: ",convertToReadableDate(latestHealthUnitRecord['start_date']))
    print("End Date: ",convertToReadableDate(latestHealthUnitRecord['end_date']))
    print("===========================")

#Get User Point
userPoint = geocoder.ip('')
userPointCheck = Feature(geometry=Point((userPoint.latlng[0],userPoint.latlng[1])))

#Convert Health Unit Strings to Polygon
waterlooHealthRegionPolygon = getPolygonFromStr(healthUnitCoordinateStrings.waterlooHealthRegionStr)
yorkRegionPolygon = getPolygonFromStr(healthUnitCoordinateStrings.yorkRegionPublicHealthStr)
huronPerthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.huronPerthHealthUnitStr)
southwesternPolygon = getPolygonFromStr(healthUnitCoordinateStrings.southwesternPublicHealthStr)
porcupineHealthUnitPolygon = getPolygonFromStr(healthUnitCoordinateStrings.porcupineHealthUnitStr)
hamiltonPublicHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.hamiltonPublicHealthServicesUnitStr)
thunderBayDistrictHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.thunderBayDistrictHealthUnitStr)
peelPublicHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.peelPublicHealthUnitStr)
lambtonPublicHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.lambtonPublicHealthUnitStr)
wellingtonDufferinGuelphHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.wellingtonDufferinGuelphHealthUnitStr)
brantCountyHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.brantCountyHealthUnitStr)
middlesexLondonHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.middlesexLondonHealthUnitStr)
sudburyAndDistrictHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.sudburyAndDistrictHealthUnitStr)
niagaraRegionPublicHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.niagaraRegionPublicHealthDepartmentStr)
chathamKentHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.chathamKentHealthUnitStr)
kingstonFrontenacLennoxAddingtonHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.kingstonFrontenacLennoxAddingtonHealthUnitStr)
windsorEssexCountyHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.windsorEssexCountyHealthUnit)
peterboroughPublicHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.peterboroughPublicHealthUnitStr)
greyBruceHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.greyBruceHealthUnitStr)
easternOntarioHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.easternOntarioHealthUnitStr)
northBayParrySoundDistrictHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.northBayParrySoundDistrictHealthUnitStr)
ottawaPublicHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.ottawaPublicHealthUnitStr)
leedsGrenvilleLanarkDistrictHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.leedsGrenvilleLanarkDistrictHealthUnitStr)
haldimandNorfolkHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.haldimandNorfolkHealthUnitStr)
timiskamingHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.timiskamingHealthUnitStr)
renfrewCountyDistrictHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.renfrewCountyDistrictHealthUnitStr)
torontoPublicHealthPolygon = getPolygonFromStr(healthUnitCoordinateStrings.TorontoPublicHealthUnitStr)



#Initialize Array of Health Units
healthUnits = [waterlooHealthRegionPolygon,yorkRegionPolygon,huronPerthPolygon,southwesternPolygon,porcupineHealthUnitPolygon,hamiltonPublicHealthPolygon,thunderBayDistrictHealthPolygon,peelPublicHealthPolygon,lambtonPublicHealthPolygon,wellingtonDufferinGuelphHealthPolygon,brantCountyHealthPolygon,middlesexLondonHealthPolygon,sudburyAndDistrictHealthPolygon,niagaraRegionPublicHealthPolygon,chathamKentHealthPolygon,kingstonFrontenacLennoxAddingtonHealthPolygon,windsorEssexCountyHealthPolygon,peterboroughPublicHealthPolygon,greyBruceHealthPolygon,easternOntarioHealthPolygon,northBayParrySoundDistrictHealthPolygon,ottawaPublicHealthPolygon,
leedsGrenvilleLanarkDistrictHealthPolygon, haldimandNorfolkHealthPolygon, timiskamingHealthPolygon, renfrewCountyDistrictHealthPolygon,torontoPublicHealthPolygon]

#Initialize Array of Healt Unit Names
healthUnitNames = ["Waterloo Health Unit","York Region Health Unit","Huron Perth Healht Unit","Southwestern Health Unit","Porcupine Health Unit",
"Hamilton Public Health Unit","Thunder Bay Health Unit","Peel Health Unit","Lambton Health Unit","Wellington Public Health Unit",
"Brant County Health Unit","Middle-Sex London Health Unit","Sudbury and District Health Unit","Niagra Public Health Unit","ChathamKent Health Unit",
"Kingston, Frontenac, Lennox and Addington Health Unit","Windsor Essex County Public Health Unit","Peterbrough Health Unit","Grey Bruce Health Unit","Eastern Ontario Health Unit",
"North Bay Parry Sound Health Unit","Ottawa Public Health Unit","Leeds, Grenville and Lanark Health Unit","Haldimand Norfolk Health Unit","Timiskaming Health Unit",
"Renfrew County District Health Unit","Toronto Health Unit"]

#Initialize Health Unit Id's
healthUnitIds = [2265,2270,5183,4913,2256,
2237,2262,2253,2242,2266,
2227,2244,2261,2246,2240,
2241,2268,2255,2233,2258,
2247,2251,2243,2234,2263,
2257,3895]
#Goes through all health units and checks which one user is located in
i = 0
for unit in healthUnits:

    #Outputs the health unit the user is in
    if boolean_point_in_polygon(userPointCheck, unit) == True:
        print("=========================================")
        print("You are Located in: ", healthUnitNames[i])
        print("=========================================")
        getHealthUnitStatusFromAPI(healthUnitIds[i])
    elif boolean_point_in_polygon(userPointCheck, unit) == False:
        print("You are Not Located in: ", healthUnitNames[i])

    
    #Checks all health unit however prints out coords    
    #print(healthUnitNames[i],"You are located in:",boolean_point_in_polygon(userPointCheck,unit))
    i+=1




