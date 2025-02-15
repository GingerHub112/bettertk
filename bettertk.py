from tkinter import *
from xml.etree.ElementTree import *

def initWindow(title, width, height):
    Win = Tk()
    Win.title(title)
    Win.geometry(f"{width}x{height}")
    return Win

def parseXML(file, root):
    tree = parse(file)
    treeRoot = tree.getroot()
    if treeRoot.tag != "view":
        raise ValueError("Root element must be 'view'")
    
    widgets = {}

    for i in treeRoot.iter():
        if i.tag == "label":
            widgets[i.attrib["id"]] = Label(root, text=i.attrib["text"], font=(i.attrib["font"], int(i.attrib["size"])))
            widgets[i.attrib["id"]].pack(pady=int(i.attrib["padding"]))
        elif i.tag == "button":
            widgets[i.attrib["id"]] = Button(root, text=i.attrib["text"], font=(i.attrib["font"], int(i.attrib["size"])))
            widgets[i.attrib["id"]].pack(pady=int(i.attrib["padding"]))
        elif i.tag == "entry":
            widgets[i.attrib["id"]] = Entry(root, font=(i.attrib["font"], int(i.attrib["size"])))
            widgets[i.attrib["id"]].pack(pady=int(i.attrib["padding"]))
        elif i.tag == "text":
            widgets[i.attrib["id"]] = Text(root, height=int(i.attrib["height"]), width=int(i.attrib["width"]), wrap="word", state=i.attrib["state"])
            widgets[i.attrib["id"]].pack(pady=int(i.attrib["padding"]))
        elif i.tag == "frame":
            widgets[i.attrib["id"]] = Frame(root)
            widgets[i.attrib["id"]].pack(pady=int(i.attrib["padding"]))

    return widgets