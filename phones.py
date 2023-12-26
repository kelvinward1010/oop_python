from items import Item

class Phone(Item):
    all_phones = []
    def __init__(self, name: str, price: float, quantity: int, broken_phone=0):
        #Call to super func to have access to all attributes
        super().__init__(name, price, quantity)
        
        #Run and test validate
        assert broken_phone >= 0, f"Broken phone {broken_phone} is not geater or equal than zero!"
        
        
        #Assign to self object
        self.broken_phone = broken_phone
        
        Phone.all_phones.append(self)
        
    def data_phone(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "broken_phone": self.broken_phone,
        }
    
    def __repr__(self) -> str:
        return f"Phone('{self.__class__.__name__} - {self.name}', '{self.price}', '{self.quantity}', '{self.broken_phone}')"
