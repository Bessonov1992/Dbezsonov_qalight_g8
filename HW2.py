class human:
    favorite_drink = "beer"
    def __init__(self,age):
        self.age = age
        if self.age < 18:
            self.favorite_drink = "juice"
    def drink(self):
        print(f"I'm {self.__class__.__name__},my favorine drink is {self.favorite_drink}!")
class worker(human):
    def __init__(self,age,salary):
        super().__init__(age)
        self.salary = salary
        if self.age >= 18 and salary > 1000:
            self.favorite_drink = "whickey"
h1 = human(17)
h1.drink()
h2 = human(18)
h2.drink()
w1 = worker(17,999)
w1.drink()
w2 = worker(18,999)
w2.drink()
w3 = worker(18,1001)
w3.drink()
w4 = worker(17,1001)
w4.drink()