
#"_something" : Indicates that the name is meant for internal use only
#"__something" : private  method
#"__something__": Call method in Python

class Item:
    @staticmethod
    def is_integer(number):
        pass
    
    
    @classmethod
    def instance_from_something(cls):
        pass
    
    def __repr__(self) -> str:
        pass
    
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value    
    
    
item = Item()
item.is_integer(5)
item.instance_from_something()