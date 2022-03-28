average = 0
sum = 0

for i in range(0,4):
    userNum = input("Please enter an input: ")
    userNum = int(userNum)
    sum = sum + userNum
    print("Your current number is: " + str(userNum) + " and your current sum is: " + str(sum))
average = sum/(i+1)

print(average)