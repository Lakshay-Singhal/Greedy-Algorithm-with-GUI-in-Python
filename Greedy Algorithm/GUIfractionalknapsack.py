from tkinter import *
import knapsackalgorithm

mainWindow = Tk()
mainWindow.title("Fractional KnapSack Problem")
mainWindow.geometry("644x344")
mainWindow.minsize(644,434)
mainWindow.maxsize(644, 434)



weights = []
values = []

frames = []
labels = []
widgets = []
capacity = 0

def getCap():
    global cap
    cap = int(ent_getCap.get())
    global lbl_gotCap
    ent_getCap.pack_forget()
    btn_getCap.pack_forget()
    lbl_getCap.pack_forget()
    lbl_gotCap.pack_forget()
    btn_addItem.pack_forget()
    lbl_gotCap = Label(mainWindow, text="Capacity of backpack: " + str(cap))
    lbl_gotCap.pack()
    btn_addItem.pack()

def createItem():
    global labels
    global frames
    global widgets

    frame = Frame(mainWindow, borderwidth=2)
    frames.append(frame)

    frame.pack(side="top")

    label= Label(frame,text="Item " + str(len(frames)) + ":   Weight: ")
    labels.append(label)
    label.pack(side="left")
    widget1 = Entry(frame,width=5,borderwidth=3)
    widget1.pack(side="left")
    label= Label(frame,text=" Cost: ")
    labels.append(label)
    label.pack(side="left")
    widget2 = Entry(frame,width=5,borderwidth=3)
    widget2.pack(side="left")

    widgets.append([widget1,widget2])

def getItems():
    global widgets
    global weights
    global values
    count=0
    btn_getItems.pack_forget()
    btn_addItem.pack_forget()
    for (wt,val) in widgets:
        weights.append(int(wt.get()))
        values.append(int(val.get()))
        label = Label(
            mainWindow,
            text="Item " + str(count)
                + ", weight: " + str(weights[count])
                + ", value: " + str(values[count])
        )
        label.pack()
        count += 1

    for frame in frames:
        frame.pack_forget()


def selectItems():
    global weights
    global values
    global lbl_maxValue
    lbl_maxValue.pack_forget()

    maxValue = knapsackalgorithm.FractionalKnapSack.getMaxValue(weights,values,cap)
    lbl_maxValue = Label(mainWindow,text="Maximum value selected from backpack: "+str(maxValue))
    lbl_maxValue.pack()

frm_getCap = Frame(mainWindow)
frm_getCap.pack()
lbl_getCap = Label(frm_getCap, text = "Capacity of backpack?", bd=5)
lbl_getCap.pack(side="left")
ent_getCap = Entry(frm_getCap)
ent_getCap.pack(side="left")
btn_getCap = Button(frm_getCap, text = "Enter", command=getCap)
btn_getCap.pack(side="left")
lbl_gotCap = Label()

btn_addItem = Button(mainWindow, text="Create Item", command=createItem, bd=3)
btn_addItem.pack()
frm_endButtons = Frame(mainWindow)
frm_endButtons.pack(side="bottom")
btn_getItems = Button(frm_endButtons, text="Save Input", command=getItems)
btn_getItems.pack(side="left")
btn_selectItems = Button(frm_endButtons, text="Get Maximum Value", command=selectItems)
btn_selectItems.pack(side="left")
lbl_maxValue = Label()

mainWindow.mainloop()
