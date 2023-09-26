import random
import datetime

print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))

today = datetime.datetime.now()
print(today)
print(today.year)

# create instance of delta class then add it to the datetime class
print(today + datetime.timedelta(days=28))

class Animal:
    name = ""
    category = ""
    
    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    category = 'reptile'

class Snake(Animal):
    category = 'reptile'

pokemon = Turtle('Blastoise')
print(pokemon.name, pokemon.category)

class Zoo:
    def __init__(self):
        self.current_animals = {}
    
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
    
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result

zoo = Zoo()

# turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(pokemon)
zoo.add_animal(snake)

print(zoo.total_of_category('reptile')) #how many zoo animal types in the reptile category