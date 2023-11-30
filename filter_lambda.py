import classes.person as p

frank = p.person()
frank.sex = "m"
frank.name = "frank"

sara = p.person()
sara.sex = "f"
sara.name = "Sara"

folks = [frank, sara]

men = filter(lambda person: person.sex == "m", folks)
women = filter(lambda person: person.sex == "f", folks)

for person in men:
	print("MALE: " + person.name)


for person in women:
	print("FEMALE: " + person.name)
