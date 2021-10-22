# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to _____"
#youtuber = "" # a sting variable 

# we have a few ways to do this 
#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))  # the format method formats the specified values and inserts them inside the strings placeholder 
#print(f"subscribe to {youtuber}") #     THIS IS THE BEST METHOD use the f string add on the beginning of the "" and then you can add the variable 


adj = input("Adjective: ")  #   2) we make the adj variable as an input and give them a prompt 
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person")   #   4) now we create the variables for verb1 verb2 and famous person 

#   1) the variable that holds the f string and we added a variable that we have not made yet 3) we then go back to this and fill more in
madlib = f"Computer programing is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"   #   3) we then add curly brackets verb1 verb2 and famous_person

print(madlib) # print the madlb variable 



# area to improve add a function to choose from random different madlibs 