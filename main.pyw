import bettertk

root = bettertk.initWindow("Bettertk example", 600, 400)
bettertk.register_command("onClick", lambda: bettertk.info_popup("This is an info message"))
bettertk.parseXML("view.xml", root)
root.mainloop()