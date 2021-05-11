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

def getPolygonFromStr(geocodesString):
    coordArray = []
    coordinates = geocodesString.split(" ")
    for coordStr in coordinates:
        coord = coordStr.split(",")
        lat = float(coord[1])
        lng = float(coord[0])
        coordArray.append((lat,lng))
    
    
    return Polygon([coordArray])

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
healthUnitNames = ["Waterloo Health Unit","York Region Health Unit","Huron Perth Healht Unit","Southwestern Health Unit","Porcupine Health Unit","Hamilton Public Health Unit","Thunder Bay Health Unit","Peel Health Unit","Lambton Health Unit","Wellington Public Health Unit","Brant County Health Unit","Middle-Sex London Health Unit","Sudbury and District Health Unit","Niagra Public Health Unit","ChathamKent Health Unit","Kingston, Frontenac, Lennox and Addington Health Unit","Windsor Essex County Public Health Unit","Peterbrough Health Unit","Grey Bruce Health Unit","Eastern Ontario Health Unit","North Bay Parry Sound Health Unit","Ottawa Public Health Unit","Leeds, Grenville and Lanark Health Unit","Haldimand Norfolk Health Unit","Timiskaming Health Unit","Renfrew County District Health Unit","Toronto Health Unit"]

#Goes through all health units and checks which one user is located in
i = 0
for unit in healthUnits:

    #Outputs the health unit the user is in
    if boolean_point_in_polygon(userPointCheck, unit) == True:
        print("=========================================")
        print("You are Located in: ", healthUnitNames[i])
        print("=========================================")
    elif boolean_point_in_polygon(userPointCheck, unit) == False:
        print("You are Not Located in: ", healthUnitNames[i])

    #Checks all health unit however prints out coords    
    #print(healthUnitNames[i],"You are located in:",boolean_point_in_polygon(userPointCheck,unit))
    i+=1




