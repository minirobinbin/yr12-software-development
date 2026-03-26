import tkinter as tk
import csv
from tkinter import filedialog
import xml.etree.ElementTree as ET

# build the root window
root = tk.Tk()
root.title("Animal Data Converter")
root.minsize(600,330)
root.maxsize(600,330)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry(f"600x330+{screenWidth//3-250}+{screenHeight//2-165}") # // gets rid of the float
animals = []
def read_csv_file():
    global animals
    file_path = filedialog.askopenfilename(title="Select CSV File",filetypes=(('csv files', '*.csv'),('All files','*.*')))
    with open(file_path,'r') as file:
        reader = csv.reader(file)
        #name,species,age,sex,sourceName,addressCity,addressState,addressCountry,notesList
        next(reader)
        rows = list(reader)

    for row in rows:
        address = row[5].split(" ")
        if len(address) == 3:
            addressCity = address[0]
            addressState = address[1]
            addressCountry = address[2]
        else:
            addressCity = address[0]
            addressState = ""
            addressCountry = address[1]
        notesList = [{'note': row[6],'date': row[7]},{'note': row[8],'date': row[9]}]
        animals.append({
            "name": row[0],
            'species': row[1],
            'age': row[2],
            'sex': row[3],
            'sourceName': row[4],
            'city': addressCity,
            'state_or_province': addressState,
            "country": addressCountry,
            'notes': notesList
        })
    # return animals
    messagetosend = ''
    for animal in range(len(animals)):
        name = animals[animal]['name']
        species = animals[animal]['species']
        age = animals[animal]['age']
        sex = animals[animal]['sex']
        sourceName = animals[animal]['sourceName']
        city = animals[animal]['city']
        state = animals[animal]['state_or_province']
        country = animals[animal]['country']
        notes = animals[animal]['notes']

        note1 = notes[0]['note']
        date1 = notes[0]['date']
        note2 = notes[1]['note']
        date2 = notes[1]['date']
        messagetosend += f'''
ANIMAL {animal + 1} ({name})
    species: {species} age: {age} sex: {sex}\n'''
        if city:
            messagetosend+= f'''    source: {sourceName}, {city}, {state},{country}\n'''
        else:
            messagetosend+= f'''    source: {sourceName}, {state},{country}\n'''
        if note1:
            messagetosend+= f'''    note({date1}): {note1}\n'''
        if note2:
            messagetosend+= f'''    note({date2}): {note2}\n'''
    readout.delete("1.0", tk.END)
    readout.insert(tk.END,messagetosend)

# print(read_csv_file())
# read_csv_file()

def saveXMLFile():
    global animals
    base = ET.Element("animals")
    tree = ET.ElementTree(base)
    for animal in animals:
        animal_element = ET.SubElement(base,"animal")
        animal_element.set("name", animal['name'])
        animal_element.set("species", animal['species'])
        animal_element.set("age", animal['age'])
        animal_element.set("sex", animal['sex'])
        source_element = ET.SubElement(animal_element,"source")

        source_element.set("name", animal['sourceName'])
        address_element = ET.SubElement(source_element,"address")
        address_element.set("city", animal['city'])
        address_element.set('state_or_province', animal['state_or_province'])
        address_element.set('country', animal['country'])

        notes_element = ET.SubElement(animal_element,"notes")
        for noteData in animal['notes']:
            if noteData['date']:
                note_element = ET.SubElement(notes_element,"note",date=noteData['date'])
                note_element.text = noteData['note']
    ET.indent(tree)
    file = filedialog.asksaveasfile(mode="w", defaultextension=".xml")
    if file:
        tree.write(file.name, encoding='utf-8', xml_declaration=True)
        file.close()

# build the widgets
importFileButton = tk.Button(root,text="Import csv file",command=read_csv_file)
textFrame = tk.Frame(root)
scrollBar = tk.Scrollbar(textFrame,orient=tk.VERTICAL)
readout = tk.Text(textFrame,width=80,height=20,yscrollcommand=scrollBar.set)
scrollBar.config(command=readout.yview)
outputButton = tk.Button(root,text="Output XML file",command=saveXMLFile)

# #place the widgets
importFileButton.pack()
textFrame.pack(expand=True,fill=tk.BOTH)
scrollBar.pack(side=tk.RIGHT,fill=tk.Y)
readout.pack(side=tk.LEFT)
outputButton.pack()

# #run mainloop
root.mainloop()