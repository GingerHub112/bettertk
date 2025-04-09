from tkinter import *
from tkinter import messagebox
from xml.etree.ElementTree import *

commands = {}

def register_command(name, func):
    """Register a command to be called when the button is pressed."""
    commands[name] = func

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
        args = {
            "bg": i.attrib.get("bg", None),
            "fg": i.attrib.get("fg", None),
            "font": (i.attrib.get("font", None), int(i.attrib.get("size", 12))),
            "width": int(i.attrib.get("width", 0)),
            "height": int(i.attrib.get("height", 0)),
            "state": i.attrib.get("state", "normal"),
            "text": i.attrib.get("text", ""),
        }

        if i.tag == "label":
            widgets[i.attrib["id"]] = Label(root, text=i.attrib["text"], font=(i.attrib["font"], int(i.attrib["size"])))
            widgets[i.attrib["id"]].pack(pady=int(i.attrib["padding"]))
        elif i.tag == "button":
            widgets[i.attrib["id"]] = Button(root, text=i.attrib["text"], font=(i.attrib["font"], int(i.attrib["size"])), command=commands.get(i.attrib["command"], None))
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

def info_popup(msg):
    messagebox.showinfo("Information", msg)

def error_popup(msg):
    messagebox.showerror("Error", msg)

def warning_popup(msg):
    messagebox.showwarning("Warning", msg)