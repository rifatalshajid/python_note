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