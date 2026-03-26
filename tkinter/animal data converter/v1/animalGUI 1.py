# python3 coding: utf-8
import csv
import tkinter as tk
from tkinter import filedialog, messagebox
import xml.etree.ElementTree as ET

# create the GUI main page
root = tk.Tk()

root.title("Animal data converter")
root.minsize(300, 330)
root.maxsize(600, 500)
# Read the screen size
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
# Centres the app in the screen on boot
root.geometry(f"585x330+{screenwidth//2-150}+{screenheight//2-150}")

# Define commands
headers = [] # holds the first line of the CSV 
animals = [] # holds each line of the CSV
output = [] # holds the output to transport to Text widget
def read_csv():
    """
    Opens and reads the input file csv file.
    Each row is stored as a dictionary with first four fields: name, species, age, sex name, 
    The next element is split into city, state_or_province and country.
    The last field notes is a list of dictionaries with their own fields: date and content.
    Any empty fields are "".
    :return: a list of dictionaries, or None if the a file I/O error occurred.
    """
    global headers, animals

    # Open a filedialog to recieve csv file
    file_path = filedialog.askopenfilename(
        title="Select CSV file",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )

    # Validtion for opening CSV file
    if not file_path:
        return
    
    try:
        with open(file_path, newline="", encoding="utf-8") as f:
            # if the file path is good, it will read the csv into a list of values in reader object
            reader = csv.reader(f)
            rows = list(reader)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open CSV:\n{e}")
        return
    
    if not rows:
        messagebox.showwarning("Empty file", "The selected CSV file is empty.")
        return

    # remove headers from the data and store for potential future use
    headers = rows.pop(0)

    for animal in rows:
        # check if country has states or provinces
        address = animal[5].split(" ")
        if len(address) == 2:
            city, country = address
            state = ''
        else:
            city, state, country = address
        
        # save animals as dictionary in a list to iterate and use for display and converting to XML
        animals.append({
            "name": animal[0],
            'species': animal[1],
            'age': animal[2],
            'sex': animal[3],
            'source': animal[4],
            'city': city,
            'state_or_province': state,
            "country": country,
            'notes': [(animal[7],animal[6]),(animal[9],animal[8])]
        })
    # clear readout widget
    readout.delete("1.0", tk.END)
    for i in range(len(animals)):
        "iterates through the animals, formats the text widgets output."

        out = f'''
ANIMAL {i+1} ({animals[i]["name"]})
  species: {animals[i]['species']} age: {animals[i]['age']} sex: {animals[i]['sex']}
  source: {animals[i]['source']}, '''
        if animals[i]['state_or_province']:
            out+=f'{animals[i]["city"]} {animals[i]['state_or_province']} {animals[i]['country']}'
        else:
            out+=f'{animals[i]["city"]} {animals[i]['country']}'
        if animals[i]['notes']!= [('',''),('','')]:
            out += f'''
  note ({animals[i]["notes"][0][0]}): {animals[i]['notes'][0][1]}'''
        if animals[i]['notes'][1]!= ("",""):
            out += f'''
  note ({animals[i]['notes'][1][0]}): {animals[i]["notes"][1][1]}'''
        
        # add the animal to a list of animals to printout
        output.append(out)
    
    # printout each animal joined by a new line
    readout.insert(tk.END, '\n'.join(output))

def save_xml_file():
    # import the list of animal dictionaries
    global animals
    # create the root element but because root is already used for Tkinter, named base
    base = ET.Element("animals")
    # create a tree with base as the root
    tree = ET.ElementTree(base)
    
    for animal in animals:
        # iterates through the animals in order to format for the xml tree
        animal_element = ET.SubElement(
            base,
            "animal"
        )
        # some animals don't have names so only include the name tag if there is one.
        if animal['name']:
            animal_element.set("name", animal['name'])
        animal_element.set("species", animal['species'])
        animal_element.set("age", animal['age'])
        animal_element.set("sex", animal['sex'])
        source_element = ET.SubElement(
            animal_element,
            "source"
        )
        source_element.set("name", animal['source'])
        address_element = ET.SubElement(
            source_element,
             "address"
            )
        address_element.set("city", animal['city'])
        if animal["state_or_province"]:
            address_element.set('state_or_province', animal['state_or_province'])
        address_element.set('country', animal['country'])
        if animal['notes'] != [("",""),("","")]:
            # if there are any notes they are written
            notes_element = ET.SubElement(
                animal_element,
                "notes"
            )
            note_element = ET.SubElement(
                notes_element,
                "note",
                date=animal['notes'][0][0]
            )
            note_element.text = animal['notes'][0][1]

            # if there is a second note, write that note
            if animal['notes'][1][0]:
                note_element = ET.SubElement(
                    notes_element,
                    "note",
                    date = animal['notes'][1][0]
                )
                note_element.text = animal['notes'][1][1]

    # pretty up the XML with indents            
    ET.indent(tree)
    # create the xml file of the tree with an XML declaration
    filename = filedialog.asksaveasfilename()
    tree.write(filename, encoding='utf-8', xml_declaration=True)
    

            

# Instantiate Widgets
import_button = tk.Button(root, text="Load CSV file", command=read_csv)

textFrame=tk.Frame(root)
scrollbar = tk.Scrollbar(textFrame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
readout = tk.Text(
    textFrame,
    wrap="word",
    yscrollcommand=scrollbar.set,
    width=80,
    height=20
    )
readout.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=readout.yview)


export_button = tk.Button(root, text="Save XML file", command=save_xml_file)

# Place the widgets
# grid the buttons and sticky them to the western wall of the grid
import_button.grid(column=1,row=1,sticky=tk.W)
textFrame.grid(column=1,row=2)
export_button.grid(column=1,row=3, sticky=tk.W)

# Run Mainloop
root.mainloop()