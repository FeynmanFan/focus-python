names = ["Smith", "Barnes", "Jones", "Behrens"]

i = 0

while(names[i] != "Jones"):
	print(names[i])
	i = i + 1

i = 0

while True:
    print(names[i])
    if (names[i] == "Jones"):
        break
    i = i + 1
