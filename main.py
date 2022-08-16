from tkmacosx import Button
import tkinter as tk
import os

# initializes a window with a title bar
root = tk.Tk(className="Inventory")
canvas = tk.Canvas(root, height=500, width=500)
canvas.pack()

################
###FRONT END####
################
def buttons():
    add_tab = Button(root, text="add item", fg="white", bg="brown", font=('times new roman', 12), command=add)
    edit_tab = Button(root, text="edit item", fg="white", bg="brown", font=('times new roman', 12), command=edit)
    view_tab = Button(root, text="view items", fg="white", bg="brown", font=('times new roman', 12), command=view)

    canvas.create_window(0, 0, window=add_tab, anchor='nw', width=166)
    canvas.create_window(253, 0, window=edit_tab, anchor='n', width=166)
    canvas.create_window(506, 0, window=view_tab, anchor='ne', width=166)

def tab_title(tab_type):
    tab = tk.Label(root, text=tab_type, font=('times new roman', 14, 'underline'), fg="white", bg="brown", width=500)
    canvas.create_window(250, 41, window=tab)


def menu_interface(interface_text):
    buttons()
    center = tk.Label(root, bg="brown")
    center2 = tk.Label(root, bg="white")
    current_tab = tk.Label(root, text=interface_text, bg="white", fg="black", font=('times new roman', 11))

    canvas.create_window(250, 250, window=center, width=250, height=250)
    canvas.create_window(250, 220, window=center2, width=220, height=100)
    canvas.create_window(250, 145, window=current_tab, width=220)


def add():
    clear_window()
    global adding_name
    global adding_location

    tab_title("Add Item")
    menu_interface("Enter information below")

    # Entry position
    name_label = tk.Label(root, text="Name of Item:", bg="white", font=('times new roman', 11))
    location_label = tk.Label(root, text="Item Location:", bg="white", font=('times new roman', 11))

    canvas.create_window(145, 190, window=name_label, anchor="w", width=80)
    canvas.create_window(145, 220, window=location_label, anchor="w", width=80)

    # Entry
    adding_name = tk.Entry(root, width=50, bg="#ffffe6")
    adding_location = tk.Entry(root, width=50, bg="#ffffe6")

    canvas.create_window(230, 190, window=adding_name, anchor="w", width=123)
    canvas.create_window(230, 220, window=adding_location, anchor="w", width=123)

    add_button = Button(root, text="Add Item", bg="brown", fg="white", font=("Times", 12), command=add_backend)
    canvas.create_window(250, 350, window=add_button, anchor="s", width=222, height=61)


def view():
    clear_window()

    begin = tk.Label(root, bg="#ffffe6")
    canvas.create_window(250, 270, window=begin, width=400, height=400)

    item_count = 0
    x, y = 55, 70
    items = load_past_items()
    for i in items:
        item = tk.Label(root, text=i, bg="#ffffe6", fg="black", font=('times new roman', 12))
        canvas.create_window(x, y, window=item, anchor="nw")
        y += 20
        item_count += 1
    item_count = "Total number of items: " + str(item_count)
    tab_title("View Items")
    items = tk.Label(root, text=item_count, fg="white", bg="brown", font=('times new roman', 12))
    canvas.create_window(425, 42, window=items)


def edit():
    clear_window()
    global find_name
    tab_title("Edit Items")
    menu_interface("Edit items below")

    name_label = tk.Label(root, text="Name of Item:", bg="white", font=('times new roman', 11))
    canvas.create_window(145, 190, window=name_label, anchor="w", width=80)

    find_name = tk.Entry(root, width=50, bg="#ffffe6")
    canvas.create_window(230, 190, window=find_name, anchor="w", width=123)

    delete_button = Button(root, text="Delete Item", bg="brown", fg="white", font=("Times", 12), command=edit_backend)
    canvas.create_window(250, 350, window=delete_button, anchor="s", width=222, height=61)


##############
###BACK END###
##############
def load_past_items():
    items = open("inventory.txt", "r")
    listing = items.readlines()  # Returns all lines in file as an item in list
    past_items = []
    for item in listing:
        current_item = item.split()  # Creates item in list of every word
        past_items.append(current_item)  # Past_items is lists of lists
    return past_items


def clear_window():
    white_window = tk.Label(root, bg="white")
    canvas.create_window(250, 250, window=white_window, width=450, height=450)


def add_backend():
    name = adding_name.get()
    location = adding_location.get()
    if not name or not location:
        return
    items = load_past_items()
    items.append([name, location])
    f = open("inventory.txt", "a")
    if os.stat("inventory.txt").st_size == 0:
        f.write(name + " " + location)
    else:
        f.write("\n" + name + " " + location)
    f.close()
    adding_name.delete(0, 'end')
    adding_location.delete(0, 'end')


def edit_backend():
    first = True
    name = find_name.get()
    items = load_past_items()
    with open("inventory.txt", "w") as f:
        for i in items:
            if i[0] != name:
                if first:
                    f.write(i[0] + " " + i[1])
                    first = False
                else:
                    f.write("\n" + i[0] + " " + i[1])
    find_name.delete(0, 'end')


##########
###MAIN###
##########

# Creating file if not already made
try:
    all_items = open("inventory.txt", "r")
except IOError:
    all_items = open("inventory.txt", "w")
    all_items.close()
else:
    all_items.close()

menu_interface("Add Item")
add()

root.mainloop()
