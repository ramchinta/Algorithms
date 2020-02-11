class robot:
    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is "+ self.name +" color is "+ self.color + " weight "+ str(self.weight))

r1 = robot('Jack','Blue',50)
r2 = robot('Tim','Green',40)

class person:
    def __init__(self,name,personality,isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting

    def sit_down(self):
        self.isSitting = True

    def stand_up(self):
        self.isSitting = False

p1 = person("Lakshman","Athletic",False)
p2 = person("Raja","Aggressive",True)

p1.robotOwned = r2
p2.robotOwned = r1

p1.robotOwned.introduce_self()
