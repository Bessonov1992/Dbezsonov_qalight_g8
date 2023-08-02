class Human:
    def __init__(self,age):
        self.age = age
    def Drink(self):
        if self.age < 18:
            self.favorite_drink = "juice"
            print(self.favorite_drink)
            print(f"Human likes drink {self.favorite_drink}")
        else:
            self.favorite_drink = "beer"
            print(self.favorite_drink)
            print(f"Human likes drink {self.favorite_drink}")

class Worker(Human):
    def __init__(self, salary, age):
        super().__init__(age)
        self.salary = salary
    def Drink(self):
        if self.salary >= 1000 and self.age >= 18:
            self.favorite_drink = "whiskey"
            print(self.favorite_drink)
            print(f"Human likes drink {self.favorite_drink}")
        elif self.salary >= 1000 and self.age < 18:
            self.favorite_drink = "whiskey"
            print(self.favorite_drink)
            print(f"Human likes drink {self.favorite_drink}")
        elif self.salary < 1000 and self.age >= 18:
            self.favorite_drink = "beer"
            print(self.favorite_drink)
            print(f"Human likes drink {self.favorite_drink}")
        else:
            self.favorite_drink = "juice"
            print(self.favorite_drink)
            print(f"Human likes drink {self.favorite_drink}")


print("First answer:\n")
h1 = Human(17)
h1.Drink()
h2 = Human(18)
h2.Drink()
h3 = Human(19)
h3.Drink()
print("\nSecond answer:\n")
w1 = Worker(999,17)
w1.Drink()
w2 = Worker(1000,17)
w2.Drink()
w3 = Worker(999,18)
w3.Drink()
w4 = Worker(1000,18)
w4.Drink()