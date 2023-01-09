##
# This program contains a superclass PoolUpgrade and 2 subclasses Sweetning and flavouring
#

# This defines the superclass PoolUpgrade
class PoolUpgrade:
    # The following 2 class variables are used to store information which is assessible to all instances of a class
    _TotalNumPoolsUpgraded = 0
    _ServiceRequestNo = 500

    # This constructor method initializes the instance variables
    def __init__(self, customerName='unknown', poolAddress='unknown', volume=0.0):
        PoolUpgrade._ServiceRequestNo += 1
        self._ServiceRequestNo = PoolUpgrade._ServiceRequestNo
        self._customerName = customerName
        self._poolAddress = poolAddress
        self._volume = volume
        PoolUpgrade._TotalNumPoolsUpgraded += 1

    # This is the get method to return the volume of pool
    def getVolume(self):
        return self._volume

    # This is the compute method to return the cost of upgrading the pool
    def computeCost(self):
        return 100 * 1.15

    # This is the str method that returns the string representation of the object
    def __str__(self):
        return ('Request No: %s \n' %self._ServiceRequestNo +
            'Customer Name: %s \n' %self._customerName +
            'Pool Address: %s \n' %self._poolAddress +
            'Pool Volume: %s cubic metres \n' %self._volume +
            'Cost: $%.2f \n' %self.computeCost())

# This defines the subclass Sweeting
class Sweetening(PoolUpgrade):
    # This constructor method initializes the instance variables of the subclass using superclass
    def __init__(self, customerName='unknown', poolAddress='unknown', volume=0.0, sweetnessLevel=0.0):
        # The following function initializes the instance variables using the superclass
        super().__init__(customerName, poolAddress, volume)
        self._sweetnessLevel = sweetnessLevel

    # This is the compute method to return the cost of upgrading the pool
    def computeCost(self):
        # The following returns the cost, using the superclass method and additional computation
        return super().computeCost() + 10 * self._volume * self._sweetnessLevel * 1.15

    # This is the str method that returns the string representation of the object
    def __str__(self):
        # The following returns the str representation, using the superclass method and additional
        return (super().__str__() +
        'Sweetness Level: %s \n' %self._sweetnessLevel)

# This defines the subclass Sweeting
class Flavouring(PoolUpgrade):
    # This constructor method initializes the instance variables of the subclass using superclass
    def __init__(self, customerName='unknown', poolAddress='unknown', volume=0, flavour='unknown'):
         # The following function initializes the instance variables using the superclass
        super().__init__(customerName, poolAddress, volume)
        self._flavour = flavour

    # This is the compute method to return the cost of upgrading the pool
    def computeCost(self):
        # The following returns the cost, using the superclass method and additional computation
        return super().computeCost() + 8 * self._volume * 1.15

    # This is the str method that returns the string representation of the object
    def __str__(self):
         # The following returns the str representation, using the superclass method and additional
        return (super().__str__() +
            'Flavour: %s \n' %self._flavour)

# This is the main tester function used to test the classes
def main():
    # The following creates a superclass and 2 subclasse objects
    one = PoolUpgrade('Jane Doe', '1 Waterway', 150)
    two = Sweetening('John Smith', '2 Puddle St', 300, 1.2)
    three = Flavouring('Jim Code', '3 Splash Rd', 240, 'Garlic')

    # Prints out the string representations of the objects
    print(one)
    print(two)
    print(three)

    # Prints out the total number of pool upgraded using the class variable TotalNumPoolsUpgraded
    print('Total number of pools upgraded: ' + str(PoolUpgrade._TotalNumPoolsUpgraded))

main()