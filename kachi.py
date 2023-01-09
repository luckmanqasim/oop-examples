##
# This program contains a Class Kachinath and its subclass Dachinath
#

# This defines the superclass Kachinath
class Kachinath:
    # This constructor method initializes the instance variables
    def __init__(self, kID='000', kName='unknown', kPowerCategory='unknown'):
        self._kID = kID
        self._kName = kName
        self._kPowerCategory = kPowerCategory

    # This is the get method to return the kID of Kachinath
    def getkID(self):
        return self._kID

    # This is the get method to return the kName of Kachinath
    def getkName(self):
        return self._kName

    # This is the get method to return the Power Category of Kachinath
    def getkPowerCategory(self):
        return self._kPowerCategory

    # This is the compute method to return the Power level of Kachinath
    def computePowerLevel(self):
        return 1.0

    # This is the str method that returns the string representation of the object
    def __str__(self):
        return ('ID: %s \n' %self._kID +
            'Name: %s \n' %self._kName +
            'Power Category: %s \n' %self._kPowerCategory +
            'Power Level: %s \n' %self.computePowerLevel())

# This is the subclass of the superclass Kachinath
class Dachinath(Kachinath):
    # This constructor method initializes the instance variables of the subclass using superclass
    def __init__(self, kID=0, kName='unknown', kPowerCategory='unknown', kLife=0.0, kFollowed='unknown'):
        # The following function initializes the instance variables using the superclass
        super().__init__(kID, kName, kPowerCategory)
        self._kLife = kLife
        self._kFollowed = kFollowed

    # This is the get method to return the kID of Dachinath
    def getkLife(self):
        return self._kLife

    # This is the get method to return the Kachinath mentor of the Dachinath
    def getkFollowed(self):
        return self._kFollowed

    # This is the compute method that computes and returns the power level of Dachinath
    def computePowerLevel(self):
        power = self._kLife * 0.005
        # IF the power is greater than 0.99, it returns 0.99
        if power > 0.99:
            return 0.99
        else:
            return power

    # This is the str method that returns the string representation of the object
    def __str__(self):
        return (super().__str__() + 'Austere Life: ' + str(self._kLife) + ' years \n' +
        'Kachinath Followed: ' + self._kFollowed + '\n')

# This is the main tester function used to test the classes
def main():
    # The following creates 2 superclass and 2 subclasse objects
    kach1 = Kachinath('1111', 'Kachilightsun', 'Light')
    kach2 = Kachinath('2222', 'Kachiflowwater', 'Flowing')
    dach1 = Dachinath('3232', 'Zaxandachi' , 'Light', 210, 'Kachilightsun')
    dach2 = Dachinath('2323', 'Xaphandachi', 'Flowing', 120, 'Kachiflowwater')

    # Prints out the string representations of the objects
    print(kach1)
    print(kach2)
    print(dach1)
    print(dach2)

main()