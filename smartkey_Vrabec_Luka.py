import tkinter as tk
import dbManager as db
from tkinter import *

root = tk.Tk()
root.title('SmartKey')
root.geometry('570x645')

########### GLOBALNE VARIJABLE ##############
var_pin = ''
var_pin_korisnik = tk.StringVar()
var_ime_korisnik = tk.StringVar()
var_prezime_korisnik = tk.StringVar()
var_aktivan_korisnik = tk.BooleanVar()

items_=()
var_korisnici = tk.Variable(value=items_)

############## FUNKCIJE #################
def setupdb():
    db_connection = db.create_connection('smartkey.db')
    
    create_table_query = ''' CREATE TABLE IF NOT EXISTS korisnici (pin INTEGER PRIMARY KEY,
                                                                   ime TEXT NOT NULL,
                                                                   prezime TEXT NOT NULL,
                                                                   aktivan BOOL);'''

    db.create_table(db_connection, create_table_query)
    db_connection = db.create_connection('smartkey.db')
    db.create_record(db_connection, (1234, 'admin', 'admin', True))

        
def pozvoni():
    text_poruke_1= tk.Label(frame1,text='Pričekajte da netko otvori vrata',borderwidth=1,relief='solid')
    text_poruke_1.place(x=185,y=25, height=20,width=220)
 
def otkljucaj():
    button_0 = tk.Button(frame2,text='0', height=3, width=6, command=lambda:button_click(button_0))
    button_1 = tk.Button(frame2,text='1', height=3, width=6, command=lambda:button_click(button_1))
    button_2 = tk.Button(frame2,text='2', height=3, width=6, command=lambda:button_click(button_2))
    button_3 = tk.Button(frame2,text='3', height=3, width=6, command=lambda:button_click(button_3))
    button_4 = tk.Button(frame2,text='4', height=3, width=6, command=lambda:button_click(button_4))
    button_5 = tk.Button(frame2,text='5', height=3, width=6, command=lambda:button_click(button_5))
    button_6 = tk.Button(frame2,text='6', height=3, width=6, command=lambda:button_click(button_6))
    button_7 = tk.Button(frame2,text='7', height=3, width=6, command=lambda:button_click(button_7))
    button_8 = tk.Button(frame2,text='8', height=3, width=6, command=lambda:button_click(button_8))
    button_9 = tk.Button(frame2,text='9', height=3, width=6, command=lambda:button_click(button_9))
    button_clear = tk.Button(frame2, text='C',height=3, width=6, command=lambda:button_click(button_clear)) 
    button_enter = tk.Button(frame2, text = 'E',height=3, width=6, command=lambda:button_click(button_enter))

    button_0.place(x=30, y=10)
    button_1.place(x=85, y=10)
    button_2.place(x=140, y=10)
    button_3.place(x=30, y=70)
    button_4.place(x=85, y=70)
    button_5.place(x=140, y=70)
    button_6.place(x=30, y=130)
    button_7.place(x=85, y=130)
    button_8.place(x=140, y=130)
    button_9.place(x=30, y=190)
    button_clear.place(x=85, y=190)
    button_enter.place(x=140, y=190)

    text_poruke = tk.Text(frame2, borderwidth=2)
    text_poruke.place(x=220, y=10, height=230, width=300)

def admin():
    admin_frame_text= tk.Label(frame1,text='U frame 3 - otvorena je administracija',borderwidth=1,relief='solid')
    admin_frame_text.place(x=185,y=25, height=20,width=220)

    #LISTBOX
    global listbox
    listbox =tk.Listbox(frame3)
    listbox.place(x=20,y=10,width=175,height=200)
    
    db_connection = db.create_connection('smartkey.db')
    dataBase_items=db.select_all_records(db_connection)

    for i in dataBase_items:

        ime_prezime= i[0],i[1],i[2],i[3]
        listbox.insert(END ,ime_prezime)

    def callback(event):
        selection = event.widget.get(event.widget.curselection())
        print(selection)
        var_pin_korisnik.set(selection[0])
        var_ime_korisnik.set(selection[1])
        var_prezime_korisnik.set(selection[2])
        var_aktivan_korisnik.set(selection[3])
      
    listbox.bind("<<ListboxSelect>>", callback)

    #LABELE
    label_obrada=tk.Label(frame3,text='Za obradu korisnika , odaberite ga iz listbox-a.')
    label_obrada.place(x=20,y=220)


    label_name=tk.Label(frame3,text='Ime',borderwidth=1, relief='solid')
    label_name.place(x=210,y=10,width=50,height=20)

    label_prezime=tk.Label(frame3,text='Prezime',borderwidth=1, relief='solid')
    label_prezime.place(x=210,y=40,width=50,height=20)
    
    label_pin=tk.Label(frame3,text='PIN',borderwidth=1, relief='solid')
    label_pin.place(x=210,y=70,width=50,height=20)

    label_aktivan=tk.Label(frame3,text='Aktivan',borderwidth=1, relief='solid')
    label_aktivan.place(x=210,y=100,width=50,height=20)

    #ENTRY ZA LABELE

    entry_name=tk.Entry(frame3,border=1,relief='solid',textvariable=var_ime_korisnik)
    entry_name.place(x=280,y=10,width=150,height=20)

    entry_prezime=tk.Entry(frame3,border=1,relief='solid',textvariable=var_prezime_korisnik)
    entry_prezime.place(x=280,y=40,width=150,height=20)

    entry_pin=tk.Entry(frame3,border=1,relief='solid',textvariable=var_pin_korisnik)
    entry_pin.place(x=280,y=70,width=150,height=20)

    nesto_aktivan=tk.Checkbutton(frame3,border=1,variable=var_aktivan_korisnik)
    nesto_aktivan.place(x=280,y=100,width=15,height=20)

    #BUTTONI
    button_spremi = tk.Button(frame3, text='Spremi',height=1, width=7,command=lambda:spremi_korisnik())
    button_spremi.place(x=210,y=150)

    button_odustani = tk.Button(frame3, text='Odustani',height=1, width=7,command=lambda:odustani_korisnik())
    button_odustani.place(x=275,y=150)

    button_izbriši = tk.Button(frame3, text='Izbriši',height=1, width=7,command=lambda:obrisi_korisnik())
    button_izbriši.place(x=340,y=150)



def button_click(button):
    global var_pin
    num_btn = ['0','1','2','3','4','5','6','7','8','9']
    if button['text'] in num_btn:
       var_pin = var_pin + button['text']
    elif button['text'] == 'C':   
       var_pin=''
    elif button['text'] == 'E':
        provjeri_pin()

def provjeri_pin():
    global var_pin
    
    db_connection = db.create_connection('smartkey.db')
    row_ = db.select_record_by_id(db_connection, var_pin)
    print(row_)
    if row_ == None:
            text_poruke = tk.Text(frame2, borderwidth=2)
            text_poruke.insert(INSERT, "Krivi PIN ! , pokušajte ponovno!")
            text_poruke.place(x=220, y=10, height=230, width=300)                       
            print('pogrešan pin')
    elif row_!= None:
        print(row_[1])
       
        if row_[1] == 'admin':
            text_poruke = tk.Text(frame2, borderwidth=2)
            text_poruke.insert(INSERT, "OTVARAM ADMIN....... ")
            text_poruke.place(x=220, y=10, height=230, width=300) 
            print('otvaram admin') 
            admin()

        elif row_[3]==False:
            text_poruke = tk.Text(frame2, borderwidth=2)
            text_poruke.insert(INSERT, "Neaktivan pin ,pristup zabranjen!")
            text_poruke.place(x=220, y=10, height=230, width=300)                       
            print('Neaktivan korisnik')
        else:        
            text_poruke = tk.Text(frame2, borderwidth=2)
            text_poruke.insert(INSERT, f"Dobrodošli  {row_[1]} , {row_[2]}!")
            text_poruke.place(x=220, y=10, height=230, width=300) 
            print('otključano') 
           
    
    var_pin = ''

def spremi_korisnik():

    db_connection = db.create_connection('smartkey.db')
   

    db.delete_record(db_connection,(var_pin_korisnik.get()))
    db_connection = db.create_connection('smartkey.db')
    db.create_record(db_connection, (var_pin_korisnik.get(),
                                    var_ime_korisnik.get(),
                                    var_prezime_korisnik.get(),
                                    var_aktivan_korisnik.get()))

    admin()

def odustani_korisnik():
    var_pin_korisnik.set('')
    var_ime_korisnik.set('')
    var_prezime_korisnik.set('')
    var_aktivan_korisnik.set(False)
    admin()
  
def obrisi_korisnik():
    db_connection = db.create_connection('smartkey.db')
    db.delete_record(db_connection,var_pin_korisnik.get())
    var_pin_korisnik.set('')
    var_ime_korisnik.set('')
    var_prezime_korisnik.set('')
    var_aktivan_korisnik.set(False)
    admin()

################# MAIN ##################
setupdb()

frame1 = tk.Frame(root, highlightbackground='black', highlightthickness=1, width=550, height=80)
frame2 = tk.Frame(root, highlightbackground='black', highlightthickness=1, width=550, height=260)
frame3 = tk.Frame(root, highlightbackground='black', highlightthickness=1, width=550, height=260)
frame1.grid(row=0, column=0, padx=10, pady=10)
frame2.grid(row=1, column=0, padx=10, pady=2)
frame3.grid(row=2, column=0, padx=10, pady=10)
frame1.pack_propagate(0)


welcome_msg= tk.Label(frame1,text='Dobrodošli , pozvonite ili ukucajte pin! ',borderwidth=1,relief='solid')
welcome_msg.place(x=185,y=25, height=20,width=210)


button_pozvoni = tk.Button(frame1, text='Pozvoni', height=3, width=15, command=pozvoni )
button_otkljucaj = tk.Button(frame1, text='otkljucaj', height=3, width=15, command=otkljucaj)
button_pozvoni.pack(side=tk.LEFT, padx=10,pady=10)
button_otkljucaj.pack(side=tk.RIGHT, padx=10,pady=10)

root.mainloop()
