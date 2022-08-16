import os
import frontend as fe

# Creating file if not already made
try:
    all_items = open("inventory.txt", "r")
except IOError:
    all_items = open("inventory.txt", "w")
    all_items.close()
else:
    all_items.close()

fe.menu_interface("Add Item")
fe.add()

fe.root.mainloop()
