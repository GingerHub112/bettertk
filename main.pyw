import bettertk
import turtle

root = bettertk.initWindow("Bettertk example", 600, 400)
bettertk.parseXML("view.xml", root)
root.mainloop()