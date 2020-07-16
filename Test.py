
class Test:
    def __init__ (self, name="no-name", mustinclucepresc=False):
        self.__name = name
        self.__mustIncluidePresc = mustinclucepresc
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
    
    def getMustInclucePresc(self):
        return self.__mustIncluidePresc

    def setMustIncludePresc(self, must):
        self.__mustIncluidePresc = must    


    def __str__(self):
        return f"Test: name : {self.__name}, mustPresc : {self.__mustIncluidePresc}"

    def __eq__(self, other):
        if(self.__name == other.getName()):
            return True
        else:
            return False