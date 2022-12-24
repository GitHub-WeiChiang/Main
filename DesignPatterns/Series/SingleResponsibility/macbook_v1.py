# 依據數值分類
class LaptopProperty: 
    cpu = ""
    size = 0
    resolution = ""

# 依據功能分類
class LaptopFunction:
    def startUp(self):
        pass

    def shutDown(self):
        pass

# 實作
class MacLaptopProperty(LaptopProperty):
    cpu = ""
    size = 0
    resolution = ""

# 實作 
class MacLaptopFunction(LaptopFunction):
    def startUp(self):
        pass
        
    def shutDown(self):
        pass

class MacBookV1:
    property: MacLaptopProperty
    function: MacLaptopFunction
    
    def __init__(self, p: MacLaptopProperty, f: MacLaptopFunction):
        self.property = p
        self.function = f

MacBookV1(MacLaptopProperty(), MacLaptopFunction())
