from os import name


class MyFunction:
    name = "Nam"
    age = 22
    male = True
    
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age

class_1 = MyFunction()
class_1.setAge(23)
class_1.getAge()
class_1.setName('Quang')
class_1.getName()

print("{} is {} years old.".format(class_1.name, class_1.age))
print("{} is {} years old.".format(MyFunction.name, MyFunction.age))
    
