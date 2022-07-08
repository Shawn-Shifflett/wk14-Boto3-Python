def dic():
    # create dict
    user = {"first_name" : "shawn"}
    print(user)
    
    # read dict
    print(user["first_name"])
    
    # update 
    user["family_name"] = "S"
    print(user)
    
    # modify
    user["family_name"] = "R"
    print(user)
    
    # delete
    del user["family_name"]
    print(user)
  
def lisst():
    fruit = ["apples", "oranges", "bananas"]
    # print the first item
    print(fruit[0])
    
    # print the length of list
    print(len(fruit))
    
    # print the last item
    print(fruit[-1])
    
    # update
    fruit.append("kiwi")
    print(fruit)
    
    # add item in the middle somewhere
    fruit.insert(2,"passion fruit")
    print(fruit)
    
    # sort list
    print(sorted(fruit))
    
    # delete
    del fruit[2]
    print(fruit)
    
def determiningType():
    v = "A STRING"
    print(type(v))
    
    i = 888
    print(type(i))


dic()
print()
lisst()
print()
determiningType()