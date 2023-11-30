import classes.person as p

frank = p.person()
frank.sex = "m"
frank.name = "frank"

sara = p.person()
sara.sex = "f"
sara.name = "Sara"

folks = [frank, sara]

def is_male(person):
	return person.sex == "m"
	
def is_female(person):
	return person.sex == "f"

men = filter(is_male, folks)
women = filter(is_female, folks)

for person in men:
	print("MALE: " + person.name)


for person in women:
	print("FEMALE: " + person.name)
