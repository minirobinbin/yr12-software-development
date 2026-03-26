import xml.etree.ElementTree as ET

# root = ET.Element("library")
# book = ET.SubElement(root, "book", attrib={"id": "1"})
# title = ET.SubElement(book, "title")
# title.text = "Python Basics"

# tree = ET.ElementTree(root)
# ET.indent(tree)
# tree.write("xml/output.xml", encoding="utf-8", xml_declaration=True)




def print_all(elem, level=0):
    indent = "  " * level
    print(f"{indent}Tag: {elem.tag}, Attributes: {elem.attrib}, Text: {elem.text.strip() if elem.text else ''}")
    
    for child in elem:
        print_all(child, level + 1)

tree = ET.parse("xml/output.xml")
root = tree.getroot()

print_all(root)
