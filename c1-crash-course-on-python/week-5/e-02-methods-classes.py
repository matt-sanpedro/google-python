# self parameter represents the instance the method is being executed on
class Piglet:
    # define attributes
    name = "piglet"
    years = 0

    def speak(self):
        # self.name will access the name attribute from the current instance
        print("Oink! I'm {}!  Oink!".format(self.name))

    def pig_years(self):
        return self.years * 18

hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

shakespeare = Piglet()
shakespeare.name = "Shakespeare"
shakespeare.speak()

piggy = Piglet()
piggy.years = 2
print(piggy.pig_years())


# __init__ special method
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    # __str__ special method that will display the string when print function is called
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

golden_apple = Apple('yellow', 'soft')
print(golden_apple.color, golden_apple.flavor)
print(golden_apple)
