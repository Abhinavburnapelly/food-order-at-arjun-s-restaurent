from tkinter import *
import tkinter.messagebox as z
from PIL import Image,ImageTk

root=Tk()
root.config(bg="grey")
root.geometry("700x800")
root.resizable(False,False)
global e1,e2,e3,e4,p1,p2,p3,p4
global pe1,pe2,pe3,pe4,pp1,pp2,pp3,pp4
global fe1,fe2,fe3,fe4,fp1,fp2,fp3,fp4
global ce1,ce2,ce3,ce4,cp1,cp2,cp3,cp4

t1="arjun's food order"
Label(text=" ",font="cosmicsms 20 normal",bg="grey").grid(row=0,column=1)
l0=Label(font="arial 16 bold",bg="white")
l0.place(x=300,y=0)
l0.config(text=t1)
root.title("arjun's restaurent")

#images

image1=image1=ImageTk.PhotoImage(Image.open("new_burger.png"))
image2=ImageTk.PhotoImage(Image.open("pizza.png"))
image3=ImageTk.PhotoImage(Image.open("french.gif"))
image4=ImageTk.PhotoImage(Image.open("cool drink.jpg"))
#burgers images
i1=ImageTk.PhotoImage(Image.open("cheese burger.jpg"))
i2=ImageTk.PhotoImage(Image.open("crispy chicken burger.jpg"))
i3=ImageTk.PhotoImage(Image.open("veg burger.jpg"))
i4=ImageTk.PhotoImage(Image.open("chicken sanwich.jpg"))
#pizza images
pi1=ImageTk.PhotoImage(Image.open("pizza1.jpg"))
pi2=ImageTk.PhotoImage(Image.open("pizza2.jpg"))
pi3=ImageTk.PhotoImage(Image.open("pizza3.jpg"))
pi4=ImageTk.PhotoImage(Image.open("pizza4.jpg"))
#french fries images
fi1=ImageTk.PhotoImage(Image.open("ff1.jpg"))
fi2=ImageTk.PhotoImage(Image.open("ff2.jpg"))
fi3=ImageTk.PhotoImage(Image.open("ff3.jpg"))
fi4=ImageTk.PhotoImage(Image.open("ff4.jpg"))
#cool drinks images
ci1=ImageTk.PhotoImage(Image.open("cd.jpg"))
ci2=ImageTk.PhotoImage(Image.open("cd2.jpg"))
ci3=ImageTk.PhotoImage(Image.open("cd3.jpg"))
ci4=ImageTk.PhotoImage(Image.open("cd4.jpg"))

#burger


label1=Label(root,font="bold")
label1.grid(row=1,column=0)
label1.config(image=image1)

#pizza


label2=Label(root,font="bold")
label2.grid(row=1,column=2)
label2.config(image=image2)

#french fries


label3=Label(root,font="bold")
label3.grid(row=3,column=0)
label3.config(image=image3)

#cool drink

label4=Label(root,font="bold")
label4.grid(row=3,column=2)
label4.config(image=image4)
#prev function
def prev():
    global e1,e2,e3,e4,p1,p2,p3,p4,preview
    global pe1,pe2,pe3,pe4,pp1,pp2,pp3,pp4,preview
    global fe1,fe2,fe3,fe4,fp1,fp2,fp3,fp4,preview
    global ce1,ce2,ce3,ce4,cp1,cp2,cp3,cp4,preview
    l0.config(text="arjun's food order ")
    label1.config(image=image1)
    label2.config(image=image2)
    label3.config(image=image3)
    label4.config(image=image4)
    b1.grid(row=2,column=0)
    b2.grid(row=2,column=2)
    b3.grid(row=4,column=0)
    b4.grid(row=4,column=2)
    preview.grid_forget()
    e1.place_forget()
    e2.place_forget()
    e3.place_forget()
    e4.place_forget()
    p1.grid_forget()
    p2.grid_forget()
    p3.grid_forget()
    p4.grid_forget()
    pe1.place_forget()
    pe2.place_forget()
    pe3.place_forget()
    pe4.place_forget()
    pp1.grid_forget()
    pp2.grid_forget()
    pp3.grid_forget()
    pp4.grid_forget()
    fe1.place_forget()
    fe2.place_forget()
    fe3.place_forget()
    fe4.place_forget()
    fp1.grid_forget()
    fp2.grid_forget()
    fp3.grid_forget()
    fp4.grid_forget()
    ce1.place_forget()
    ce2.place_forget()
    ce3.place_forget()
    ce4.place_forget()
    cp1.grid_forget()
    cp2.grid_forget()
    cp3.grid_forget()
    cp4.grid_forget()

#order
def order():
    global total_burger
    total_burger=int(e1.get())*10+int(e2.get())*25+int(e3.get())*12+int(e4.get())*15
    total_pizza=int(pe1.get())*10+int(pe2.get())*25+int(pe3.get())*12+int(pe4.get())*15
    total_ff=int(fe1.get())*10+int(fe2.get())*25+int(fe3.get())*12+int(fe4.get())*15
    total_cd=int(ce1.get())*10+int(ce2.get())*25+int(ce3.get())*12+int(ce4.get())*15
    
    total_cost=total_burger+total_pizza+total_ff+total_cd
    z.showinfo("price",f"total bill of burger is:{total_burger}\n total bill of pizza:{total_pizza}\n total bill of french fries:{total_ff}\n total bill of cool drinks:{total_cd}\ntotal cost:{total_cost}")
    


#burger function
def burger():
    
    
    l0.config(text="burgers menu")
    label1.config(image=i1)
    label2.config(image=i2)
    label3.config(image=i3)
    label4.config(image=i4)
    b1.grid_forget()
    b2.grid_forget()
    b3.grid_forget()
    b4.grid_forget()
    
    global p1,p2,p3,p4,preview
    p1=Label(text="$10",font="arial 15 normal")
    p1.grid(row=2,column=0)
    global e1,e2,e3,e4
    e1=Entry(root,width=5,textvariable=IntVar())
    e1.place(x=200,y=345)
    p2=Label(text="$25",font="arial 15 normal")
    p2.grid(row=2,column=2)
    e2=Entry(root,width=5,textvariable=IntVar())
    e2.place(x=500,y=345)
    p3=Label(text="$12",font="arial 15 normal")
    p3.grid(row=4,column=0)
    e3=Entry(root,width=5,textvariable=IntVar())
    e3.place(x=200,y=685)
    p4=Label(text="$15",font="arial 15 normal")
    p4.grid(row=4,column=2)
    e4=Entry(root,width=5,textvariable=IntVar())
    e4.place(x=500,y=685)
    
    
    
    Button(text="order now",font="hervatica 20 bold",command=order).grid(row=5,column=2,pady=5)
    preview= Button(text="prev",font="hervatica 20 bold",command=prev)
    preview.grid(row=5,column=0)

#pizza function
def pizza():
    l0.config(text="pizza menu")
    label1.config(image=pi1)
    label2.config(image=pi2)
    label3.config(image=pi3)
    label4.config(image=pi4)
    b1.grid_forget()
    b2.grid_forget()
    b3.grid_forget()
    b4.grid_forget()
    
    global pp1,pp2,pp3,pp4,preview
    pp1=Label(text="$10",font="arial 15 normal")
    pp1.grid(row=2,column=0)
    global pe1,pe2,pe3,pe4
    pe1=Entry(root,width=5,textvariable=IntVar())
    pe1.place(x=200,y=345)
    pp2=Label(text="$25",font="arial 15 normal")
    pp2.grid(row=2,column=2)
    pe2=Entry(root,width=5,textvariable=IntVar())
    pe2.place(x=500,y=345)
    pp3=Label(text="$12",font="arial 15 normal")
    pp3.grid(row=4,column=0)
    pe3=Entry(root,width=5,textvariable=IntVar())
    pe3.place(x=200,y=685)
    pp4=Label(text="$15",font="arial 15 normal")
    pp4.grid(row=4,column=2)
    pe4=Entry(root,width=5,textvariable=IntVar())
    pe4.place(x=500,y=685)
    
    
    
    Button(text="order now",font="hervatica 20 bold",command=order).grid(row=5,column=2,pady=5)
    preview= Button(text="prev",font="hervatica 20 bold",command=prev)
    preview.grid(row=5,column=0)

#french fries
def french_fries():
    l0.config(text="french fries menu")
    label1.config(image=fi1)
    label2.config(image=fi2)
    label3.config(image=fi3)
    label4.config(image=fi4)
    b1.grid_forget()
    b2.grid_forget()
    b3.grid_forget()
    b4.grid_forget()
    
    global fp1,fp2,fp3,fp4,preview
    fp1=Label(text="$10",font="arial 15 normal")
    fp1.grid(row=2,column=0)
    global fe1,fe2,fe3,fe4
    fe1=Entry(root,width=5,textvariable=IntVar())
    fe1.place(x=200,y=345)
    fp2=Label(text="$25",font="arial 15 normal")
    fp2.grid(row=2,column=2)
    fe2=Entry(root,width=5,textvariable=IntVar())
    fe2.place(x=500,y=345)
    fp3=Label(text="$12",font="arial 15 normal")
    fp3.grid(row=4,column=0)
    fe3=Entry(root,width=5,textvariable=IntVar())
    fe3.place(x=200,y=685)
    fp4=Label(text="$15",font="arial 15 normal")
    fp4.grid(row=4,column=2)
    fe4=Entry(root,width=5,textvariable=IntVar())
    fe4.place(x=500,y=685)
    
    
    
    Button(text="order now",font="hervatica 20 bold",command=order).grid(row=5,column=2,pady=5)
    preview= Button(text="prev",font="hervatica 20 bold",command=prev)
    preview.grid(row=5,column=0)

#cool drink
def cool_drink():
    l0.config(text="drink's menu")
    label1.config(image=ci1)
    label2.config(image=ci2)
    label3.config(image=ci3)
    label4.config(image=ci4)
    b1.grid_forget()
    b2.grid_forget()
    b3.grid_forget()
    b4.grid_forget()
    
    global cp1,cp2,cp3,cp4,preview
    cp1=Label(text="$10",font="arial 15 normal")
    cp1.grid(row=2,column=0)
    global ce1,ce2,ce3,ce4
    ce1=Entry(root,width=5,textvariable=IntVar())
    ce1.place(x=200,y=345)
    cp2=Label(text="$25",font="arial 15 normal")
    cp2.grid(row=2,column=2)
    ce2=Entry(root,width=5,textvariable=IntVar())
    ce2.place(x=500,y=345)
    cp3=Label(text="$12",font="arial 15 normal")
    cp3.grid(row=4,column=0)
    ce3=Entry(root,width=5,textvariable=IntVar())
    ce3.place(x=200,y=685)
    cp4=Label(text="$15",font="arial 15 normal")
    cp4.grid(row=4,column=2)
    ce4=Entry(root,width=5,textvariable=IntVar())
    ce4.place(x=500,y=685)
    
    
    
    Button(text="order now",font="hervatica 20 bold",command=order).grid(row=5,column=2,pady=5)
    preview= Button(text="prev",font="hervatica 20 bold",command=prev)
    preview.grid(row=5,column=0)

#BUTTONS
#burger buttons
b1=Button(root,font="cosmicsms 15 normal",command=lambda:burger())
b1.grid(row=2,column=0)
b1.config(text="press")
#pizza buttons
b2=Button(root,font="cosmicsms 15 normal",command=pizza)
b2.grid(row=2,column=2)
b2.config(text="press")

#french button
b3=Button(root,font="cosmicsms 15 normal",command=french_fries)
b3.grid(row=4,column=0)
b3.config(text="press")


#cool drink buttons
b4=Button(root,font="cosmicsms 15 normal",command=cool_drink)
b4.grid(row=4,column=2)
b4.config(text="press")




root.mainloop()