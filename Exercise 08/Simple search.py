#Initialize the list of names
names =("Jake", "Zac", "Ian", "Ron", "Sam", "Dave")
def simple_term(name_list,search_term):
    if search_term in name_list:
     return f"'{search_term}'found in list"
    else:
        return f"'{search_term}' not found in list"
    
    # searching for sam
    search_term = "sam"
print ("Simple___ name (name, search_name)")

#Allow to the user input targets
target= input ("enter the name of search")

#Implement the search functionality
result = 'Simple___name'(names,target)
print(result)
