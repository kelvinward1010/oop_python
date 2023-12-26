from items import Item
from phones import Phone
from keyboard import Keyboard

item1 = Keyboard("Item default", 300, 2)

# item1.name = "My Item"

item1.apply_increment(0.3)

print(item1)

print(item1.send_email())