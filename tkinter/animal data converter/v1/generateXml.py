from xml.dom import minidom

def generatev1(name,species,age,sex,sourceName,addressCity,addressState,addressCountry,notesList):
    rootmain = minidom.Document()

    animal = rootmain.createElement('animal')
    animal.setAttribute('name',name)
    animal.setAttribute('species',species) 
    animal.setAttribute('age',age) 
    animal.setAttribute('sex',sex) 
    rootmain.appendChild(animal)

    source = rootmain.createElement('source')
    source.setAttribute('name',sourceName)
    animal.appendChild(source)

    address = rootmain.createElement('address')
    address.setAttribute('city',addressCity)
    address.setAttribute('state_or_province',addressState)
    address.setAttribute('country',addressCountry)
    source.appendChild(address)

    # adding notes

    notes = rootmain.createElement('notes')
    animal.appendChild(notes)

    for noteData in notesList:
        note = rootmain.createElement('note')
        note.setAttribute('date', noteData['date'])
        date_text = rootmain.createTextNode(noteData['note']) 
        note.appendChild(date_text)
        notes.appendChild(note)

    xml_str = rootmain.toprettyxml(indent ="\t") 
    xml_str = "\n".join(xml_str.split("\n")[1:])

    save_path_file = "tkinter/animal data converter/gfg.xml"

    with open(save_path_file, "a") as f:
        f.write(xml_str) 


import xml.etree.ElementTree as ET
def generatev2(animals):
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
