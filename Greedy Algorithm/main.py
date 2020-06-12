from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import time
import subprocess
root=Tk()

root.geometry("644x434")
root.title("Greedy Algorithms")
root.minsize(644,434)
root.maxsize(644, 434)
root.configure(bg="black")


def frac():
    subprocess.call(['python','GUIfractionalknapsack.py'])

def job():
    subprocess.call(['python','_activitySelection_gui.py'])

def huffman():
    subprocess.call(['python','GHuffman.py'])

def kruskal():
    subprocess.call(['python','GKruskal.py'])

def dijkstra():
    subprocess.call(['python','GDijkstra.py'])
def credit():
    messagebox.showinfo(title="Credits", message='''                    B. Tech.   CSE 2nd Year

                    Kaushiki Taru      -   18103053
                    Kumari Soni        -   18103054
                    Lakshay Singhal    -   18103055

Dr. B. R. Ambedkar National Instiitute of Technology''')





class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", fg="cyan2",bg="black", font=("Helvetica", 18))
        self.label.place(x=275,y=2)
        self.update_clock()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)

app=App(root)
root.after(1000, app.update_clock)

heading1=Label(text="Main Screen" ,bg="black", fg="white", font=("Helvetica", 20))
heading1.place(x=245,y=35)
heading=Label(text="Greedy Algorithms with GUI" ,bg="black", fg="white", font=("Helvetica", 20))
heading.place(x=160,y=70)


heading=Label(text="Press respective button to implement desired algorithm:-" ,bg="black", fg="cyan2", font=("Helvetica", 13))
heading.place(x=130,y=120)

myFont = font.Font(weight="bold",size=11)

b1 = Button(root,width=30,bg="azure2", fg="black", text="Fractional Knapsack",borderwidth = '4',command=frac, relief=RAISED )
b1['font'] = myFont
b1.place(x=95,y=200)

l1=Label(text="T={O(NlogN)}" ,bg="azure",width=18, fg="black", font=myFont)
l1.place(x=380,y=205)


b2 = Button(root, bg="azure2", fg="black",width=30, text="Activity Selection Problem",borderwidth = '4', command=job, relief=RAISED)
b2['font'] = myFont
b2.place(x=95,y=280)

l2=Label(text="T={O(N logN)}" ,bg="azure",width=18, fg="black", font=myFont)
l2.place(x=380,y=285)

b3 = Button(root, bg="azure2", fg="black",width=30,  text="Huffman coding",borderwidth = '4', command=huffman, relief=RAISED)
b3['font'] = myFont
b3.place(x=95,y=240)

l3=Label(text="T={O(nlogn)}" ,bg="azure",width=18, fg="black", font=myFont)
l3.place(x=380,y=245)


b4 = Button(root, bg="azure2", fg="black",width=30, text="Kruskal's Algorithm",borderwidth = '4', command=kruskal, relief=RAISED)
b4['font'] = myFont
b4.place(x=95,y=160)

l4=Label(text="T={O(ElogE)}" ,bg="azure",width=18, fg="black", font=myFont)
l4.place(x=380,y=165)



b5 = Button(root, bg="azure2", fg="black",width=30, text="Dijkstra's algorithm",borderwidth = '4', command=dijkstra, relief=RAISED)
b5['font'] = myFont
b5.place(x=95,y=320)

l5=Label(text="T={O(V+E)}" ,bg="azure",width=18, fg="black", font=myFont)
l5.place(x=380,y=325)


b6 = Button(root, bg="azure2", fg="black",width=50, text="Credits",borderwidth = '4', command=credit)
b6['font'] = myFont
b6.place(x=95,y=360)

#Label(text="Lakshay Singhal, 18103055" ,bg="black", fg="white", font=("Helvetica", 12)).place(x=360,y=405)
#Label(text="Kumari Soni, 18103054" ,bg="black", fg="white", font=("Helvetica", 12)).place(x=360,y=380)
#Label(text="Kaushiki Taru, 18103053" ,bg="black", fg="white", font=("Helvetica", 12)).place(x=360,y=355)

root.mainloop()




