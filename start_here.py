from tkinter import Tk, font, font
import tkinter
from youtube_downloader import Moj_YouTube
from pytube import YouTube
from tkinter import *
link = ''

master = Tk()
master.title('YouTube Downloader')
master.geometry("600x250")
mojfont = font.Font(family='Arial',size=16,weight='bold')
linki = tkinter.Entry(master=master,font=mojfont)
Label(master,text='Podaj link do filmu: ',font=mojfont).place(x=0,y=0)

linki.pack()

def lak():
    link = linki.get()
    if Moj_YouTube.Start(link) == None:
        yt = YouTube(link)
        tytul = Moj_YouTube(yt).tytul
        autor = Moj_YouTube(yt).autor
        wyswietlenia = Moj_YouTube(yt).wyswietlenia
        tytul1 = Label(master,text=f'Tytuł  =  {tytul}',font=mojfont)
        tytul1.pack()
        autor1 = Label(master,text=f"Autor  =  {autor}",font=mojfont)
        autor1.place(x=0,y=100)
        wyswietlenia1 = Label(master,text=f'Wyświetlenia  =  {wyswietlenia}',font=mojfont)
        wyswietlenia1.place(x=0,y=150)
        def mp3przycisk():
            Moj_YouTube(yt).MP3(yt)
        def mp4przycisk():
            Moj_YouTube(yt).MP4(yt)
        
        tkinter.Button(master,text='Pobierz w formacie MP3',command=mp3przycisk).place(x=400,y=150)
        tkinter.Button(master,text='Pobierz w formacie MP4',command=mp4przycisk).place(x=400,y=200)
    else:
        print("Wrong input")
    
        
    
    
    return None


tkinter.Button(master,text="Szukaj",command=lak).pack()






#Wykonali: Maksym Bernasiewicz, Piotr Suchomski, Mateusz Mercik, Adrian Kowalewski
master.mainloop()

