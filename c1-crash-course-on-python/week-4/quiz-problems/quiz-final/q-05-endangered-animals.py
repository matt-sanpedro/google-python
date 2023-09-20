def endangered_animals(animal_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.    
    for animal in animal_dict.keys(): 
        # Use a string method to format the required string.
        result += "{} \n".format(animal)
    return result


print(endangered_animals({"Javan Rhinoceros":60, "Vaquita":10, "Mountain Gorilla":200, "Tiger":500}))

# Should print:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger