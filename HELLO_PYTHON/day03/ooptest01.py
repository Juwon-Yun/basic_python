class Animal:
    def __init__(self):
        self.age = 1
        print("Animal: __init__")
        
    def getOlder(self):
        self.age += 1
        
    def __del__(self):
        print("Animal: __del__")
    
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.nonrijuk_sago = 0
        print("Human: __init__")
        
    def getDdit(self):
        self.nonrijuk_sago += 100
        
    def __del__(self):
        print("Human: __del__")
            
if __name__ == '__main__':    
    h = Human()
    print(h.age)
    print(h.nonrijuk_sago)
    h.getOlder()
    h.getDdit()
    print(h.age)
    print(h.nonrijuk_sago)

        