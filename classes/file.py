class file:
    def __init__(self, fileName, size, created):
        self.fileName = fileName
        self.size = size
        self.created = created
        
    def save(self):
        pass
        #persist the file to the hard drive
        
    @staticmethod
    def create(fileName, size, created):
        return file(fileName, size, created)