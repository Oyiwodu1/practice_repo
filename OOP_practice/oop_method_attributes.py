class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):  #study is a method name we can choose. eat, sleep, 
        print(f"{self.name} is studying")

    def introduce(self):
        print(f"My name is {self.name}")
student1 = student("Faith", 25)
student1.study()
student1.introduce()