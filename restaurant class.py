class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print("Restaurant Name is", self.name, " And cuisine is ", self.cuisine_type)


    def open_restaurant(self):
        print("Restaurant is open")


restaurant1 = Restaurant("Dilli Darbar", "Indian")
restaurant2 = Restaurant("Ladoo gopal", "Indian")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
