from tkinter import *
from datetime import date

root = Tk()
root.title('Getting Started With Widgets')
root.geometry('400x300')

lbl = Label(text="Lets Multiply Two Numbers",fg = "white",bg='#023020',height=1,width=300)

n1_label = Label(text="Enter Number 1",bg='#4F7942',fg="black")
n1_entry = Entry()

n2_label = Label(text="Enter Number 2",bg='#4F7942',fg="black")
n2_entry = Entry()

def multiply():
    
    n1 = int(n1_entry.get())
    n2 = int(n2_entry.get())
    product = n1*n2
    
    text_box.insert(END,f"Here's The Final Product...\n{n1} x {n2} = {product}")
    
    
text_box = Text(height = 3)
btn = Button(text = "Calcualte", command = multiply,height= 1, bg= '#8A9A5B',fg='white')

lbl.pack()
n1_label.pack(pady=5)
n1_entry.pack(pady=5)
n2_label.pack(pady=5)
n2_entry.pack(pady=5)
btn.pack(pady=3)
text_box.pack(pady=5)

root.mainloop()
    
    