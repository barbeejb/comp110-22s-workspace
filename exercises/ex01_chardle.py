"""EX01 - Chardle - A cute step toward Wordle."""
___Author___ = "730366585"

word = input("Enter a 5-character word: ")

if len(word) != 5:
    print("Error: Word must be 5 characters")
    quit()
else:    
    character = input("Enter a single character: ")
instance = int(0)
#Sets Variables and corrects user for wrong inputs


if len(character) == 1:
    print( "Searching for ", character, "in ", word )
else:
    print("Error: Character must be a single character.")
    quit()
#Checks Length of Character


if character == word[0]:
    print(character, "found at index 0")
    instance = instance + 1
if character == word[1]:
    print(character, "found at index 1")
    instance = instance + 1
if character == word[2]:
    print(character, "found at index 2")
    instance = instance + 1
if character == word[3]:
    print(character, "found at index 3")
    instance = instance + 1
if character == word[4]:
    print(character, "found at index 4")
    instance = instance + 1
#Checks instances for letter


if instance == 1:
    print(instance, "instance found of", character, "in", word)

else: 
    if instance > 1:
        print(instance, " instances found of", character, "in", word)
    else:
        print("No Instances of", character, "in", word) 
        #Outputs based on number of instances.