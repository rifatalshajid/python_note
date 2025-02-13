class father:
    car = "BMW"
    Home = "Two Flat"
    Money = "20c"
    Business = "Stationary"


class son(father):
    
    brokenHome = "Broken Home"
    LostProject = "Lost Project"

Broker = son()

print(Broker.Money)
print(Broker.LostProject)



# Multiple inheritance -------------------

class Grandfather:
    Money = "55c"
    Business = "Five business"
    Laptop = "Apple"

class GrandMother:
    Money = "50c"
    Business = "Ten business"
    Laptop = "Intel"

class Father:
    Money = "20c"
    Business = "Two business"
    Laptop = "Dell"
    Mobile = "iPhone"

class Son(Grandfather, GrandMother, Father):
    Mobile = "Samsung"
    Business = "Zero Business"
    Bike = "Yamaha"


b = Son()

print(b.Business)



# Multilavel inheritance ============== 

class Father:
    Smartphone = "Iphone"
    Ac = "Walton"
    Microphone = "Logitech"

class Son1(Father):
    Headphone = "mi"
    Laptop = "HP"

class Son2(Son1):
    Earbuds = "Realme"
    SmartWatch = "Mibro"

class Son3(Son2):
    Bike = "Yamaha"
    Camera = "Canon"

k = Son3

print(k.Bike)
