class a:
    name="raja"
    def __init__(self,ss1):
        self.ss1=ss1
obj1=a("sam")
obj2=a("go")
print("play is boy{}".format(obj1.__class__.name))
print("go is boy{}".format(obj2.__class__.name))
print("car is {}".format(obj1.ss1))
print("name is {}".format(obj2.ss1))

class car:
    def __init__(self,name):
        self.name=name
    def luxury(self):
        print("Its a costly car for{}".format(self.name))
c=car("BMW") 
c1=car("BENTLEY")
c.luxury()
c1.luxury()           
