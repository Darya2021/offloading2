class Cat:
    def __init__ (self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def hello(self):
        print("hello! my name is {}!".format(self.name))

pishi = Cat("pishi", 3, "red")
pishi.name = "gorbe"
pishi.hello()
