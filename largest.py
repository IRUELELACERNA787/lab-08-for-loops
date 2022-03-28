largest = 0

for i in range(0,4):
    userInput = input("Please enter a number: ")
    userInput = int(userInput)

    if(userInput > largest):
        largest = userInput
    else:
        largest = largest
    print("The current User Input is: " + str(userInput) + " and the current largest value is: " + str(largest))

print("The largest value is: " + str(largest))