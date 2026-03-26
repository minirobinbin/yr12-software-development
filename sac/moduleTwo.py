import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os

# get the running directory
script_path = os.path.abspath(__file__)
folder = os.path.dirname(script_path)

data = [] # create a data list
def readCSV(mode):
    global data
    if mode == "start": # inital start to get supply.csv from the directory
        # print("inital")
        try:
            with open(f'{folder}/supply.csv', 'r') as supply:
                reader = csv.reader(supply)
                next(reader)
                for row in reader:
                    data.append({
                        'type': row[0],
                        'colour': row[1],
                        'quantity': row[2],
                        'counted': 0
                    })
        except:
            messagebox.showerror("Hi Windows!", "Error: supply.csv not found! Press Ok to choose file")
            readCSV('update')
    elif mode == 'update': # backup statement if there is no supply.csv
        # print("backup")
        file_path = filedialog.askopenfilename(title="Select CSV File",filetypes=(('csv files', '*.csv'),('All files','*.*')))
        try:
            with open(file_path, 'r') as supply:
                reader = csv.reader(supply)
                next(reader)
                for row in reader:
                    data.append({
                        'type': row[0],
                        'colour': row[1],
                        'quantity': row[2],
                        'counted': 0
                    })
        except:
            messagebox.showerror("Hi Windows!", "Error: supply.csv not found!")

# print(data)
# print(len(data))

current = 0
def showdata(): # function to display data to the GUI
    global current
    # print(current)
    brikTypeData.config(text=f"{data[current]['type']}")
    brikColourData.config(text=f"{data[current]['colour']}")
    brikOutOfLabel.config(text=f"out of {data[current]['quantity']}")
    spinBox.config(to=data[current]['quantity'])
    spinBox.delete(0,tk.END)
    spinBox.insert(0,data[current]['counted'])

def saveData(): #function to save the counted values into output.csv
    counted = spinBox.get()
    data[current]['counted'] = counted
    with open(f'{folder}/output.csv','w') as output:
        writer = csv.DictWriter(output,fieldnames=["Type", "Colour", "Quantity","Counted"])
        writer.writeheader()
        for brik in data:
            writer.writerow({
                "Type": brik["type"],
                "Colour": brik["colour"],
                "Quantity": brik["quantity"],
                "Counted": brik["counted"]
            })
    messagebox.showinfo("Hi Windows!", "Saved counted.csv!") 


def move(direction): # function to control and change data values, saving the current counted values
    global current
    if direction == 'back' and current != 0:
        counted = spinBox.get()
        data[current]['counted'] = counted
        current = current- 1
        # print(current)
        showdata()
    elif direction == "forward" and current+1 < len(data):
        counted = spinBox.get()
        data[current]['counted'] = counted
        current = current+ 1
        # print(current)
        showdata()
    else:
        # print("error")
        messagebox.showerror("Hi Windows!", "Error: No more to show")

# create GUI window
root = tk.Tk()
root.title("Supply Counting Helper")
root.minsize(270,150)
root.maxsize(270,150)
# configure the grid for the tkinter window
root.columnconfigure((0,2),weight=1)
root.columnconfigure(1, weight=3)
root.rowconfigure(((1,2)), weight=1)
root.rowconfigure(0,weight=4)

# create the frame like the mockup
frame = tk.Frame(root, relief='solid', bd=2)
frame.grid(row=0,column=1,sticky='NESW',pady=6)
# configure the grid for the tram
frame.columnconfigure((0,1,2),weight=1)
frame.rowconfigure(((0,1,2)), weight=1)

#create and place widgets
brikTypeLabel = tk.Label(frame,text="Type")
brikTypeLabel.grid(row=0, column=0, sticky="NESW")
brikTypeData = tk.Label(frame,text="")
brikTypeData.grid(row=0, column=1, sticky="W")

brikColourLabel = tk.Label(frame,text="Colour")
brikColourLabel.grid(row=1, column=0, sticky="NESW")
brikColourData = tk.Label(frame,text="")
brikColourData.grid(row=1, column=1, sticky="W")

brikCountedLabel = tk.Label(frame,text="Counted")
brikCountedLabel.grid(row=2, column=0, sticky="NESW")

spinBox = tk.Spinbox(frame, from_=0, to=20, width=3, relief="sunken")
spinBox.grid(row=2, column=1, sticky="NESW")
brikOutOfLabel = tk.Label(frame,text="out of ")
brikOutOfLabel.grid(row=2, column=2, sticky="NESW")

previousButton = tk.Button(root, text="Previous",width=5, command=lambda: move("back"))
nextButton = tk.Button(root, text='Next',command=lambda: move("forward"))
saveButton = tk.Button(root, text="Save to counted.csv", command=saveData)

# place buttons
previousButton.grid(row=1,column=1,sticky='WN')
nextButton.grid(row=1,column=1,sticky='N')
saveButton.grid(row=2,column=1,sticky='E')

readCSV("start") # inital read call when the program starts
showdata() # show the first brik type on startup

#fancy menubar action to change supply.csv (dont worry about this bahhahahahah)
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='Update', menu=filemenu)
filemenu.add_command(label='update supply.csv data', command=lambda: readCSV("update"))

# run mainloop
root.mainloop()



#---------------------+-----------------+-----------------+------------+--------------+
#   action            | expected result |  actual result  | pass/fail  |    remedy    |
#---------------------+-----------------+-----------------+------------+--------------+
# start with no supply| manual selection|      crash      |    fail    | add function |
#       file          |                 |                 |            |to choose file|
#---------------------+-----------------+-----------------+------------+--------------+
# counted > quantity  |     block       | accepts value   |    fail    | spinbox max  |
#---------------------+-----------------+-----------------+------------+--------------+
# next/previous exceed|  error          | error           |    pass    |              |
#  index              |  notification   | notification    |            |              |
#---------------------+-----------------+-----------------+------------+--------------+

#+---------------------------+--------------------------+----------------------+
#|        input              |        process           |        output        |
#+---------------------------+--------------------------+----------------------+
#|        supply.csv         |  1. display brik type    |    save output.csv   |
#|      counted values       |  2. save counted value   |                      |
#+---------------------------+--------------------------+----------------------+