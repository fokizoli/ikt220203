from tkinter import *
ablak1 = Tk()
gyoker = 'C:\\Users\\fokizoltan\\gitfz\\ikt220203\\'
ablak1.geometry('450x450')
ablak1.title('IKT Tkinter')
icon = PhotoImage(file=gyoker+'phone-receiver-silhouette.png')
ablak1.iconphoto(True, icon)
ablak1.config(background='black')
elsokep = PhotoImage(file=gyoker+'light-png.png')
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

ablak1.mainloop()

