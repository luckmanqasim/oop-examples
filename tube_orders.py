##
# This program contains a TubeOrder Class, to generate order objects for the tubes
#

import math

# This defines the Limurian class
class TubeOrder:
    # These are the class variables, which are used to store info which is accessible to all instances of a class
    _NoOfOrders = 0
    _NextOrderID = 1000

    # This is the constructor method, which is used in initialzing the instance of a class
    def __init__(self, quantityOrdered=0, radius1=0.0, radius2=0.0, height=0.0):
        # Following increments the class variable
        TubeOrder._NoOfOrders += 1
        # Following instance variables are used in constructing the object
        self._orderID = TubeOrder._NextOrderID
        self._quantityOrdered = quantityOrdered
        self._radius1 = radius1
        self._radius2 = radius2
        self._height = height
        # Following increments the class variable
        TubeOrder._NextOrderID += 2

    # This get method returns the OrderID
    def getID(self):
        return self._orderID

    # This get method returns the object height
    def getHeight(self):
        return self._height

    # This get method returns the quantity ordered
    def getQuantityOrdered(self):
        return self._quantityOrdered

     # This set method updates the radius1 variable with a new value passed as argument
    def setRadius1(self, newRad):
        self._radius1 = newRad
        print('The radius1 of tubes for Order ID %s has been changed to %.2f.'  %(self._orderID, self._radius1))
        # The following print statements prints out the new total cost of the instance object
        print('The new cost for Order ID %s is $%.2f. \n' %(self.getID(), self.getTotalCost()))

     # This set method updates the radius2 variable with a new value passed as argument
    def setRadius2(self, newRad):
        self._radius2 = newRad
        print('The radius2 of tubes for Order ID %s has been changed to %.2f.'  %(self._orderID, self._radius2))
        # The following print statements prints out the new total cost of the instance object
        print('The new cost for Order ID %s is $%.2f. \n' %(self.getID(), self.getTotalCost()))

     # This set method updates the height variable with a new value passed as argument
    def setHeight(self, newHeight):
        self._height = newHeight
        print('The height of tubes for Order ID %s has been changed to %.2f.'  %(self._orderID, self._height))
        # The following print statements prints out the new total cost of the instance object
        print('The new cost for Order ID %s is $%.2f. \n' %(self.getID(), self.getTotalCost()))

    # This get method computes and returns the thickness of the tube
    def getThickness(self):
        return self._radius1 - self._radius2

    # This get method computes and returns the total surface area of all tubes in an order
    def getTotalSurfaceArea(self):
        calc = self._quantityOrdered * (2 * math.pi * (self._radius1 * self._height + self._radius2 * self._height + (math.pow(self._radius1, 2) - math.pow(self._radius2, 2))))
        return calc

    # This get method computes and returns the total cost of all tubes in an order
    def getTotalCost(self):
        total_cost = (0.5 * self.getTotalSurfaceArea()) * 1.15
        return total_cost

    # This special method returns the following info about the TubeOrder object, if the str() method is called onto it
    def __str__(self):
        return ('Order ID: %s \n' %self._orderID +
            'Quantity Ordered: %s tubes \n' %self._quantityOrdered +
            'Tube Outside Radius: %s cm \n' %self._radius1 +
            'Tube Inside Radius: %s cm \n' %self._radius2 +
            'Tube Height: %s cm \n' %self._height +
            'Tube Thickness: %s cm \n' %self.getThickness() +
            'Total Surface Area: %.2f sq.cm. \n' %self.getTotalSurfaceArea() +
            'Total Cost (with tax): $%.2f \n' %self.getTotalCost())

# This is the main tester function used to test the classes
def main():
    # The following list contains the TubeOrders
    orders = [TubeOrder(100, 10, 5, 15), TubeOrder(300, 9.5, 7.5, 20)]

    # Following prints the string representation of the 2 TubeOrder objects
    for order in orders:
        print(order)

    # The following updates the height of the TubeOrder object
    orders[1].setHeight(30)

    # The following print statements prints out the total number of orders, using the class var
    print('The total number of orders received was ' + str(TubeOrder._NoOfOrders) + '. \n')

    # TOTAL COST OF ALL ORDERS
    total_cost = 0
    # This for loop, loops over all TubeOrder objects and adds the cost of each to total_cost to creat total
    for order in orders:
        total_cost += order.getTotalCost()
    print('The total cost of all orders received was $%.2f.' %total_cost)


main()