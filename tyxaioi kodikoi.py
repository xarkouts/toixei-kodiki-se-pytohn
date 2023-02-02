from tkinter import *
import random
kodikos=" "
def genitria_kodikon():
    kefalea="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mikra=kefalea.lower()
    arithmi=""
    for i in range(0,10):
     arithmi=arithmi+str(i)
    simbola="[]{}()*:/,._-@!#$%^&*"
    ola=kefalea+mikra+arithmi+simbola
    mikos=16
    kodikos="".join(random.sample(ola,mikos))
    apotelesma["text"]=kodikos
root=Tk()
root.title("tixei kodiki")
root.geometry("400x200")
root.geometry()
perigrafi=Label(root,text="παραγωγη τυχαιου κωδικου")
perigrafi.pack()
btn=Button(root,text="generate",bg="yellow",command=genitria_kodikon)
btn.pack(padx="20",pady="20")
apotelesma=Label(root,text="")
apotelesma.pack()
root.mainloop()

