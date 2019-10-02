# Session 3 Exercises

# Section A

# Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango
# Add "Grapes" to the list
# Change "Pears" to "Strawberries"
# Remove "Apples" from the list
# Print out the current length of the list
# Loop through the list and print out all items
# Order the list alphabetically
# Print out all the items again
# Section B

# Create the following dictionary for an apple: Type = "Bramley", Price = 0.39, Colour = "Green"
# Add the best before date to the Dictionary
# Change the price to 0.41
# Set the apple to be on offer using a Boolean
# Print out all the key/value pairs of the apple
# The offer has now expired, remove the key/value from the Dictionary
# Section C

# Ask the user to enter a persons name, if they enter a name, ask for the persons age. Store this information in a dictionary inside a list. Continue to ask for names until no name is given. Then print out all of the names and ages collected

fruits = ["Apples", "Cherries", "Pears", "Pineapples", "Peaches", "Mango"]
print(fruits)

fruits.append("Grapes")
print(fruits)

fruits[2] = "Strawberries"
print(fruits)

del fruits[0]
print(fruits)

print(len(fruits))

for fruit in fruits:
    print(fruit)
    
fruits.sort()
print(fruits)

apple = {
    "Type": "Bramley", 
    "Price": 0.39,
    "Colour": "Green"
}
print(apple)

apple["BestBeforeDate"] = "07/08/2019"
print(apple)

apple["Price"] = 0.41
print(apple)

apple["OnOffer"] = True
print(apple)

for value in apple:
    print(str(value) + " = " + str(apple[value]))

del (apple["OnOffer"])
print(apple)

people = []
name = input("Enter a persons name: ")
while len(name) != 0:
    age = input("Enter the person's age: ")
    people.append({
        "Name": name,
        "Age": age
    })
    name = input("Enter another person's name: ")
print(people)