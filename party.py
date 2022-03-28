partyCountdown = input("How long until the party starts? ")
partyCountdown = int(partyCountdown)

if(partyCountdown < 1):
    print("PARTY NOW!!!")
else:
    for i in range(partyCountdown, 0, -1):
        print(str(i))
    print("PARTY TIME!!!")