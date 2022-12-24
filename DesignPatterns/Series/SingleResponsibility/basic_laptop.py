# 全部放在一起
class Laptop: 
    cpu = ""
    size = 0
    
    def startUp(self):
        pass
    
    def shutDown(self): 
        pass

# 實作接口
class BasicLaptop(Laptop):
    cpu = ""
    size = 0
    
    def startUp(self):
        pass
    
    def shutDown(self):
        pass

BasicLaptop()
