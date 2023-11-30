import classes.person as p

frank = p.person()
frank.sex = "m"
frank.name = "frank"

sara = p.person()
sara.sex = "f"
sara.name = "Sara"

folks = [frank, sara]

men = map(lambda person: person.name, filter(lambda person: person.sex == "m", folks))
women = filter(lambda person: person.sex == "f", folks)

for name in men:
	print("MALE: " + name)

for person in women:
	print("FEMALE: " + person.name)
