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
    """Outputs the apple color and flavor defined when instantiated"""
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    # __str__ special method that will display the string when print function is called
    # GOOD practice: how class used to define a __str__method
    """Prints the attributes of the Apple class"""
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

golden_apple = Apple('yellow', 'soft')
print(golden_apple.color, golden_apple.flavor)
print(golden_apple)
print(help(Apple))

def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes, and seconds"""
    return hours*3600 + minutes*60 + seconds
help(to_seconds)

# Jupyter notebook code, elevator exercise
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
    def up(self):
        """Makes the elevator go up one floor."""
        self.current += 1
        if self.current > self.top:
           self.current = self.top
        return self.current
    def down(self):
        """Makes the elevator go down one floor."""
        # cannot go below floor 1
        self.current -= 1
        if self.current < self.bottom:
           self.current = self.bottom
        return self.current
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        if self.current > self.top:
           self.current = self.top
        elif self.current < self.bottom:
           self.current = self.bottom
        return self.current
    def __str__(self):
        return "Current floor: {}".format(self.current)

elevator = Elevator(-1, 10, 0)
