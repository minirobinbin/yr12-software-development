import csv
import os
import tkinter as tk


script_path = os.path.abspath(__file__)
folder = os.path.dirname(script_path)

participants = []
def readCSV():
    with open(f"{folder}/participants.csv",'r') as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            participants.append({"first name": line[0],'surname': line[1],"age": int(line[2])})
    # print(participants)
def allocate():
    global participants
    groups = {}
    teens = []
    seniors = [] 
    adults = []
    size = spinBox.get()
    amountOfGroups = len(participants)/int(size)
    # print(amountOfGroups)
    for person in participants:
        if person['age'] <18:
            teens.append(person)
        elif person['age'] > 60:
            seniors.append(person)
        else:
            adults.append(person)
    # print(teens)
    group_count = min(len(teens), len(seniors))
    for group in range(group_count):
        groups[group] = [teens[group], seniors[group]]
    
    print(len(groups[1]))
    
    
    for person in adults:
        if len(groups)
    

    readout.insert(tk.END,groups)

    # readout.delete("1.0", tk.END)
    # readout.insert(tk.END,teens)
    # readout.insert(tk.END,seniors)
    # readout.insert(tk.END,adult)

# create GUI window
root = tk.Tk()
root.title("Team Allocator")
root.minsize(750,500)
root.maxsize(750,500)
# configure the grid for the tkinter window
root.columnconfigure(0,weight=3)
root.columnconfigure(1, weight=4)
root.rowconfigure(0, weight=2)
root.rowconfigure(1,weight=4)

# create widgets
teamLabel = tk.Label(root,text="Team size: ")
spinBox = tk.Spinbox(root, from_=4, to=8, width=2, relief="sunken")
allocatedLabel = tk.Label(root,text="Allocated teams:")
allocatedButton = tk.Button(root,text="Allocate",command=allocate) # button
textFrame = tk.Frame(root)
scrollBar = tk.Scrollbar(textFrame,orient=tk.VERTICAL)
readout = tk.Text(textFrame,width=80,height=30,yscrollcommand=scrollBar.set)
scrollBar.config(command=readout.yview)
textFrame.grid(row=1, column=1, sticky="NESW")
# place widgets
teamLabel.grid(row=0,column=0,sticky="W")
spinBox.grid(row=0,column=0,sticky="E")
allocatedButton.grid(row=1,column=0,sticky="WNE")
allocatedLabel.grid(row=0,column=1,sticky='NWS')
textFrame.grid(row=1,column=1,sticky="NESW")
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
readout.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

readCSV()
# run mainloop
root.mainloop()
