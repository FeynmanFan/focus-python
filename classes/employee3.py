class employee: 
	firstName = ""
	lastName = ""
	salary = 0.0

    def setLastName(value):
        if (len(value) < 1024:
            lastName = value;
        else:
            # do something else
            
    def getLastName():
        return lastName;

    lastName = property(getLastName, setLastName)
    
#employee.lastName = "Behrens"
#print(employee.lastName)