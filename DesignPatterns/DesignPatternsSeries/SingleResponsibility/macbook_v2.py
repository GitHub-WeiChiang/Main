# 數值接口
class LaptopBasicProperty: 
    cpu = ""
    size = 0

# 數值擴充接口
class LaptopExtensionProperty:
    resolution = ""

# 功能接口
class LaptopBasicFunction:
    def startUp(self):
        pass

    def shutDown(self):
        pass

# 功能擴充接口
class LaptopExtensionFunction:
    def sleep(self):
        pass

# 實作
class MacLaptopBasicProperty(LaptopBasicProperty):
    cpu = ""
    size = 0

# 實作
class MacLaptopExtensionProperty(LaptopExtensionProperty):
    resolution = ""

# 實作
class MacLaptopBasicFunction(LaptopBasicFunction):
    def startUp(self):
        pass

    def shutDown(self):
        pass

# 實作
class MacLaptopExtensionFunction(LaptopExtensionFunction):
    def sleep(self):
        pass

# 整合
class MacBookV2:
    basic_property: MacLaptopBasicProperty
    basic_function: MacLaptopBasicFunction
    extension_property: MacLaptopExtensionProperty
    extension_function: MacLaptopExtensionFunction
    
    def __init__(self, bp: MacLaptopBasicProperty, bf: MacLaptopBasicFunction, ep: MacLaptopBasicFunction, ef: MacLaptopExtensionFunction):
        self.basic_property = bp
        self.basic_function = bf
        self.extension_property = ep
        self.extension_function = ef

MacBookV2(MacLaptopBasicProperty(), MacLaptopBasicFunction(), MacLaptopBasicFunction(), MacLaptopExtensionFunction())