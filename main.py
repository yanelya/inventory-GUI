import functionality as f

# Creating file if not already made
try:
    all_items = open("inventory.txt", "r")
except IOError:
    all_items = open("inventory.txt", "w")
    all_items.close()
else:
    all_items.close()

f.menu_interface("Add Item")
f.add()

f.root.mainloop()
