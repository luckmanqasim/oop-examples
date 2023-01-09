##
# This program contains a Limurian Class, which holds information about beings called Limurians
#

# This defines the Limurian class
class Limurian:
    # These are the class variables, which are used to store info which is accessible to all instances of a class
    _population = 1500
    _lim_ID_Generator = 3000
    _LIMSPEED = 5000

    # This is the constructor method, which is used in initialzing the instance of a class
    def __init__(self, limName, distanceFromOrig):
        # Following two increment the class variables
        Limurian._lim_ID_Generator += 2
        Limurian._population += 1
        # Following instance variables are used in constructing the object
        self._limName = limName
        self._limID = str(Limurian._lim_ID_Generator) + self._limName[0:3]
        self._distanceFromOrig = distanceFromOrig

    # This get method returns the LimID
    def getLimID(self):
        return self._limID

    # This get method returns the distance from planet Lemuria to the Limurian’s original home planet
    def getDistance(self):
        return self._distanceFromOrig

    # This set method updates the distanceFromOrig variable with a new value passed as argument
    def updateDistance(self, newDist):
        oldDist = self._distanceFromOrig
        self._distanceFromOrig = newDist
        print('The distance to original planet for Limurian with ID ' + str(self._limID) +
         ' has been updated from ' + str(oldDist) + ' limmetres to ' + str(self._distanceFromOrig) +
         ' limmetres. \n')

    # This method computes and returns the time to travel between Lemuria and the original planet
    def computeTravelTime(self):
        return 2 * self._distanceFromOrig / Limurian._LIMSPEED

    # This special method returns the following info about the Limurian object, if the str() method is called onto it
    def __str__(self):
        return ('ID: %s \n' %self._limID +
            'Name: %s \n' %self._limName +
            'Distance to original planet: %s limmetres \n' %self._distanceFromOrig +
            'Travel time to and from original planet: %.1f limminutes \n' %self.computeTravelTime())

# This is the main tester function used to test the classes
def main():
    # The following creates 3 limurian objects
    limurians = [Limurian('Shrilim', 15000), Limurian('Centaurilim', 25000), Limurian('Bhavlim', 45000)]

    # Following prints the string representation of the 3 limurian objects
    for lim in limurians:
        print(lim)

    # The following updates the distance of a limurian object
    limurians[1].updateDistance(200000)

    # The following print statement prints out the total population of the Limurian planet
    print('The current population of planet Lemuria is ' + str(Limurian._population) + '.')

main()