# special magic methods / dunder methods
# operator overloading
# polymorphism ----> method overriding

class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f"{self.brand} {self.model}"

    # str , repr
    def __str__(self):
        return f'{self.brand} {self.model}'

    def __repr__(self):
        return f'Phone({self.brand}, {self.model}, {self.price})'

    def __len__(self):
        return len(self.phone_name())

    # def __add__(self, other):
        # return self.price + other.price 


class Smartphone(Phone):
    def __init__(self, brand, model, price, camera):
        super().__init__(brand, model, price)
        self.camera = camera

    def phone_name(self):
        return f"{self.brand} {self.model} and price is {self.price}"

# 2 + 3 = 5
# 'abc' + 'def' = 'abcdef'

# l = [1,2,3]
# print(len(l))
# t = (1,2,3)
# s = 'harsit'
# print(len(t))
# print(len(s))


my_phone = Phone('nokia','1100',1000)
my_phone2 = Phone('nokia','1600',1200)
my_smartphone = Smartphone('oneplus','5t',33000,'16 MP')
print(my_smartphone.phone_name())
print(my_phone.phone_name)



# print(my_phone + my_phone2)
# print(len(my_phone))
# print(str(my_phone))
# print(repr(my_phone))
# print(my_phone.__repr__())
    
