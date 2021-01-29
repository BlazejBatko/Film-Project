import os
import tkinter as tk
from xml.dom.minidom import parse
import xml.dom.minidom
from tkinter import filedialog
DOMTree = xml.dom.minidom.parse('XML.xml')
collection = DOMTree.documentElement

movies = collection.getElementsByTagName("movie")


def Wypisz():
    print(entry.get())


root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=800, bg='white')
canvas.pack()
background_image = tk.PhotoImage(file='tlo.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#d7e0dd')
frame.place(relx=0.1, rely=0.20, relwidth=0.8, relheight=0.7)
# ENTRY POLE
entry = tk.Entry(root, bg='white', justify='center', font=('Courier New', 15, 'italic'), bd=1)
entry.insert(1, 'The Godfather')
entry.place(relx=0.1, rely=0.08, relheight=0.07, relwidth=0.8)

wpisana = entry.get()
wpisana_nowa = ""
tytul_label = tk.Message(root)

def openfile():
    xmlfile = filedialog.askopenfilename()
    os.system('C:/Users/R7 1700/PycharmProjects/pythonProject/XML.xml')

def WypiszSzukana(wpisana):
    title2 = tk.StringVar()
    rank2 = tk.StringVar()
    rating2 = tk.StringVar()
    votes2 = tk.StringVar()

    for movie in movies:
        title = movie.getElementsByTagName('title')[0]
        if wpisana == title.childNodes[0].data:
            print("****MOVIE*****")
            title = movie.getElementsByTagName('title')[0]
            title2.set("Tytuł: %s" % title.childNodes[0].data)
            rank = movie.getElementsByTagName('rank')[0]
            rank2.set("Pozycja w rankingu: %s " % rank.childNodes[0].data)
            rating = movie.getElementsByTagName('rating')[0]
            rating2.set("Oceny: %s " % rating.childNodes[0].data)
            votes = movie.getElementsByTagName('votes')[0]
            votes2.set("Liczba Głosów: %s " % votes.childNodes[0].data)

            tytul_label = tk.Message(frame, textvariable=title2, width=500, font=('helvetica neue', 15,'italic', 'bold' ), bg='white')
            tytul_label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.05)

            rank_label = tk.Message(frame, textvariable=rank2, width=300, font=('helvetica neue', 15, 'italic', 'bold'), bg='white')
            rank_label.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.05)

            rating_label = tk.Message(frame, textvariable=rating2, width=300, font=('helvetica neue', 15, 'italic', 'bold'), bg='white')
            rating_label.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.05)

            votes_label = tk.Message(frame, textvariable=votes2, width=300, font=('helvetica neue', 15, 'italic', 'bold'), bg='white')
            votes_label.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.05)
            wpisana_nowa = wpisana
            return
    Czyszczenie()


def Czyszczenie():

    var = tk.StringVar()
    frame2 = tk.Frame(root, bg='#d7e0dd')
    frame2.place(relx=0.1, rely=0.20, relwidth=0.8, relheight=0.7)
    var.set("Podany film\nnie występuje w bazie danych")
    var_label = tk.Message(frame2, textvariable=var, width=500, justify='center', font=('helvetica neue', 15, 'bold', 'italic'), bg='#d7e0dd', fg = 'red')
    var_label.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.2)

    var_label.after(3900, lambda: var_label.destroy())

    frame2.after(4000, lambda: frame2.destroy())
    
    entry.insert(1, wpisana_nowa)


# PRZYCISK WYSZUKAJ
button = tk.Button(root, font=('Courier New', 15,), text="Wyszukaj film", width=68, bd=1, fg='white', bg='black',
                   command=lambda: WypiszSzukana(entry.get()))

buttonopen = tk.Button(root, font=('Courier New', 9,), text="Otworz w przegladarce", width=68, bd=1, fg='white', bg='black', command=openfile)
wpisana = entry.get()
button.place(rely=0.92, relx=0.1, relwidth=0.8, relheight=0.07)
buttonopen.place(rely=0.01, relx=0.1, relwidth=0.30, relheight=0.04)

root.mainloop()
