class Dog:
    def __init__(self):
        self.flag_bark = True
        print("Dog: __init__")
    def doMouseCover(self):
        self.flag_bark = False
        
class Bird:
    def __init__(self):
        self.fly_skill = 0
        print("Bird: __init__")
    def getOlder(self):
        self.fly_skill += 1
        
class GaeSae(Dog, Bird):
    def __init__(self):
        Dog.__init__(self)
        Bird.__init__(self)
        print("GaeSae: __init__")
    
    def __del__(self):
        print("GaeSae: __del__")
    
if __name__ == '__main__':
    g = GaeSae()
    print(g.flag_bark)
    print(g.fly_skill)
    g.doMouseCover()
    g.getOlder()
    print(g.flag_bark)
    print(g.fly_skill)