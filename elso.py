from tkinter import *
def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a + b
    mezo3.delete(0, END)
    mezo3.insert(0, 'Összeg: '+str(c))
foablak=Tk()
cimke=Label(foablak, text='Üdvözlet!', fg='red')
cimke.pack()
gomb1=Button(foablak, text='OK')
gomb1.pack()
gomb2=Button(foablak, text='Mégse')
gomb2.pack()
gomb3=Button(foablak, text='Kilépés', command=foablak.destroy)
gomb3.pack()
mezo1=Entry(foablak)
mezo1.pack()
mezo2=Entry(foablak)
mezo2.pack()
gomb4=Button(foablak, text='Osszead', command=osszeg)
gomb4.pack()
mezo3=Entry(foablak)
mezo3.pack()


can1 = Canvas(foablak, width =460, height =460, bg ='white')
photo = PhotoImage(file ='giphy.gif')
#photo = PhotoImage(file ="light-png.png")
item = can1.create_image(80, 80, image =photo)
can1.pack()


foablak.mainloop()