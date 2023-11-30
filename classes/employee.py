class employee: 
    def __init__(self):
        self._firstName = ""
        self._lastName = ""
        salary = 0.0
    
    def __del__(self):
        pass
    
    def setFirstName(self, value):
        # firstnames of greater than 1024 will cause a buffer overrun
    
        if len(value) < 1024:
            self._firstName = value

    def getFirstName(self):
        return self._firstName
        
    def setLastName(self, value):
        if len(value) < 1024:
            self._lastName = value

    def getLastName(self):
        return self._lastName

    firstName = property(getFirstName, setFirstName)
    lastName = property(getLastName, setLastName)
    
    def salaryOpinion(self):
        if (self.salary > 100000):
            return "fat stacks"
        else:
            return"Working man"