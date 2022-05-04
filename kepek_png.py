from tkinter import *
def klikk():
       print('Klikkeltem')
ablak1 = Tk()
gyoker = 'C:\\Users\\fokizoltan\\gitfz\\ikt220203\\'
ablak1.geometry('600x600')
ablak1.title('IKT Tkinter')
icon = PhotoImage(file=gyoker+'phone-receiver-silhouette.png')
ablak1.iconphoto(True, icon)
ablak1.config(background='black')
menusor = Frame(ablak1)
menusor.pack(side=TOP, fill=X)
menu1 = Menubutton(menusor, text="Fájl", underline=0)
menu1.pack(side= LEFT)
fajl = Menu(menu1)
fajl.add_command(label="Névjegy", command=klikk)
fajl.add_command(label="Kilép", command=ablak1.destroy)
menu1.config(menu=fajl)
elsokep = PhotoImage(file=gyoker+'giphy.gif')
gombkep = PhotoImage(file=gyoker+'giphy.gif', width='50', height='50')
cimke = Label(ablak1,
             text='Üdvözlet!',
             fg='#553388',
             bg="#c3cee0",
             font=('Arial', 45, 'bold'),
             bd=10,
             relief=RAISED,
             padx=45,
             pady=30,
             image=elsokep,
             compound='center'
          ).pack()

gomb = Button(ablak1,
               text= 'Kattints!',
               fg='blue',
               font=('Comic Sans', 35, 'bold'),
               bg='yellow', 
               relief=SUNKEN,
               bd=10,
               command=klikk,
               padx=12,
               pady=12,
               image=gombkep,
               compound="bottom",
               activebackground='blue',
               activeforeground='yellow',
               state=ACTIVE).pack()

ablak1.mainloop()

