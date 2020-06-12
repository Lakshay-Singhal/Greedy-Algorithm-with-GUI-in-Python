from tkinter import *
from huffmancoding import *

root = Tk()
root.title("Huffman Coding Problem")
root.geometry("644x344")
root.minsize(644,434)
root.maxsize(644, 434)
root.configure(bg="black")

#Heading
Label(root, text="Huffman Coding", fg="white",bg="black", font=("Helvetica", 25)).place(x=180,y=5)
Label(root, text="Welcome User", fg="white",bg="black", font=("Helvetica", 18)).place(x=220,y=55)

#Text for our form
st = Label(root, text="Enter the String : ", fg="white",bg="black", font=("Helvetica", 14))

#Pack text for our form
st.place(x=145,y=100)

# Tkinter variable for storing entries
stvalue = StringVar()

#Entries for our form
stentry = Entry(root, textvariable=stvalue)

# Packing the Entriest
stentry.place(x=300,y=105)

def getvals():
    print(f"{stvalue.get()} ")

    with open("huffmanrecords.txt", "a") as f:
        f.write(f"{stvalue.get()}\n\n")
    huffmanalgo(f"{stvalue.get()}")
    

Button(text="Find result",bg="azure2", fg="black",width=30, command=getvals).place(x=180,y=130)


root.mainloop()








