class student:
    def __init__(self,name,height,age,number):
        self.height =height
        self.age = age
        self.number = number
        self.name = name

    def grow(self,height=7):
        self.height += height



anton=student("Anton",193,13,45756754785)
print("name - ",anton.name)
print("height - ",anton.height)
print("age - ",anton.age)
print("number - ",anton.number)

anton.grow(height=7)
print(anton.height)
