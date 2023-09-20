def alphabetize_lists(list1, list2):


  new_list = [] # Initialize a new list.
  new_list = list1 + list2 # Combine the lists.
  new_list.sort() # Sort the combined lists.
#   new_list = ___ # Assign the combined lists to the "new_list".
  return new_list 


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]


print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']
