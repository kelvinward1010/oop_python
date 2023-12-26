import csv
from typing import Any

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str ="default", price: float = 0, quantity: int = 0):

        #Run and test validate
        assert price >= 0, f"Price {price} is not geater or equal than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not geater or equal than zero!"
        
        
        #Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        #Actions to be executed
        Item.all.append(self)
        
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if 0 < len(value) <= 12:
            self.__name = value
        else:
            raise Exception("The name is too long!")
        
    @property
    def price(self):
        return self.__price
 
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
    
    
    def data(self) -> dict:
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
        }
        
    def calculator_total(self):
        self.total = self.__price * self.quantity
        return self.total
    
    
    @classmethod
    def instance_from_csv(cls):
        with open('items.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
            
        for item in items:
            Item(
                name= str(item['name']),
                price= float(item['price']),
                quantity= int(item['quantity']),
            )
    
    @staticmethod
    def is_integer(num):
        #we will count out the floats that are point zero
        if isinstance(num, float):
            #Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __repr__(self) -> str:
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"
    
    
    def __connect(self, connection):
        pass
    
    def __prepare_body(self):
        return f"""
            Hello world!
            My name is Kelvin Ward
            We have {self.name} and {self.price} nows
        """
        
    def __send(self):
        pass
        
    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()
        
        return self.__prepare_body()
    
    
    
