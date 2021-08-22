import math


class CityDistance:
    """ Returns the flight distance between two cities given their latitude and longitude coordinates. """

    def __init__(self) -> None:
        # Initializing latitutde and longitude values for both cities 
        self.lat1 = 0.0
        self.lat2 = 0.0
        self.long1 = 0.0
        self.long2 = 0.0


    def acceptInput(self):
        # Try except block
        try:
            # Accepting Coordinates of both cities
            self.lat1, dir1, self.long1, dir2 = input(' > City 1 : ').split()
            self.lat2, dir3, self.long2, dir4 = input(' > City 2 : ').split()
            self.lat1, self.long1, self.lat2, self.long2 = \
                float(self.lat1), float(self.long1), float(self.lat2), float(self.long2)  
        except:
            # In case of error print valid message
            print('\nInvalid input entered. Please enter input in the following format : \n City 1: 51.5074 N, 0.1278 W\n')
            # Recursively call the function again to accept input
            self.acceptInput()


    def calculateDistance(self):
        # Calculate difference of latitude and longitude
        del_lat = math.radians(self.lat2 - self.lat1)
        del_long = math.radians(self.long2 - self.long1)

        # Convert latitutdes from degrees to radians
        lat1 = math.radians(self.lat1)
        lat2 = math.radians(self.lat2)
        # Radius of the Earth - in km
        RADIUS = 6372.8

        # Use Haversine's Formula for calculating the distance
        a = math.sin(del_lat/2)**2 + math.cos(lat1)*math.cos(lat2)*(math.sin(del_long/2)**2)
        dist = 2 * RADIUS * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Print the final answer
        print("\nCity 1 and City 2 are {distance} km apart.".format(distance=dist))


# Creating instance of class CityDistance
obj = CityDistance()
# Accept co-ordinates of both cities
obj.acceptInput()
# Calculate and print flight distance between both cities.
obj.calculateDistance()

