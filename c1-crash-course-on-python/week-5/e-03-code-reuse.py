# inheritance: example with __init__ special method
class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

granny_smith = Apple('green', 'tart')
carnelian = Grape('purple', 'sweet')

print(granny_smith.flavor)
print(carnelian.flavor)

# inheritance: example with initialized attribute "sound"
class Animal:
    sound = ''
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("{sound} I'm {name}!  {sound}".format(name=self.name, sound=self.sound))

class Piglet(Animal):
    sound = "Oink"

piggy = Piglet("Miss Piggy")
piggy.speak()

class Cow(Animal):
    sound = 'Mooooo'

milky = Cow('Milky White')
milky.speak()

# composition
class Repository:
    # always initialize mutable attributes in the constructor
    def __init__(self):
        self.packages = {}

    # method for adding packages
    def add_package(self, package):
        self.packages[package.name] = package

    # calculate size of whole repository
    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result

# composition
# reuse the Clothing.stock attribute and stock_by_material() function of the Clothing class to take stock of the Cotton shirts and pants!
class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)