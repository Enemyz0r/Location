# Dependencies: geopy

from geopy.geocoders import Nominatim
from geopy.distance import vincenty

class Location:
    """Calculate distance (in km) between two locations"""

    def __init__(self, loc1='', loc2=''):
        self.loc1 = loc1
        self.loc2 = loc2

    def getLoc1(self):
        """Get first location."""
        self.loc1 = input("Enter the first location: ")

    def getLoc2(self):
        """Get second location."""
        self.loc2 = input("Enter the second location: ")

    def distance(self):
        """Calculate distance between Loc1 and Loc2
        Returns:
            Distance - distance between the two locations
        """
        geolocator = Nominatim()
        location1 = geolocator.geocode(self.loc1, language='en') # get latitude and longitude of city1
        location2 = geolocator.geocode(self.loc2, language='en') # get latitude and longitude of city2

        Loc1 = (location1.latitude, location1.longitude) # create a set of latitude and longitude for city1
        Loc2 = (location2.latitude, location2.longitude) # create a set of latitude and longitude for city2

        coordToKm = round(vincenty(Loc1, Loc2).kilometers, 2) # use vincenty function to convert lat and long of cities into a single distane in km
        Distance = print("Distance between {} and {} is: {} km.".format(self.loc1, self.loc2, coordToKm))

        return Distance

def main():
       c = Location()
       c.getLoc1()
       c.getLoc2()
       c.distance()

if __name__=='__main__':
    main()
