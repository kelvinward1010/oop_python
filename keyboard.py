from items import Item

class Keyboard(Item):
    def __init__(self, name: str, price: float, quantity: int):
        #Call to super func to have access to all attributes
        super().__init__(name, price, quantity)
        
    
        