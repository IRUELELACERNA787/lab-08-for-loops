myData = {"effective top tube length": 515, "seat tube length": 500, "seat tube angle": 74.4, "head tube angle": 70.5, "stack": 513, "reach": 367, "standover height": 755}

myKeys = [] #[]] is an empty array 
myValues = []

#Parallel Iteration

for k, v in myData.items():
    #k and v are incremental variables, iterating simultaneously.
    #.items is a METHOD that allows us to iterate as many times as there are "items" in our dictionary.

    print("key: " + str(k) + ", value " + str(v)) #Monitor status of each variable on each iteration!

    myKeys.append(k)
    myValues.append(v)

print("ALL KEYS: " + str(myKeys))
print("ALL VALUES: " + str(myValues))