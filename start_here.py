import tkinter
from tkinter import *
from tkinter import font, simpledialog
from pytube import YouTube
from moviepy.editor import *
import os
class Moj_YouTube:
    def __init__(self,yt):
        self.tytul = yt.title
        self.autor = yt.author
        self.wyswietlenia = yt.views
    def MP4(yt,tytul2):
        pobier = yt.streams.get_highest_resolution()
        pobier.download(filename=f'{tytul2}.mp4')
    def MP3(yt,tytul2):    
        pobierz = yt.streams.get_lowest_resolution()
        pobierz.download(filename=f"{tytul2}.mp4")
        video = VideoFileClip(os.path.join(f"{tytul2}.mp4"))
        video.audio.write_audiofile(os.path.join(f"{tytul2}.mp3"))
        video.close()
        os.remove(f"{tytul2}.mp4")  
    def Start(link):
            yt = YouTube(link)
            zgadza_sie = yt.check_availability()
            return(zgadza_sie)
master = Tk()
master.title('YouTube Downloader')
master.geometry("600x250")
master.resizable(False,False)
mojfont = font.Font(
    family='Arial',
    size=16,
    weight='bold')
pobieranie_font = font.Font(
    family='Times',
    size=20,
    weight='bold',
)
linki = tkinter.Entry(master=master, font=mojfont)
linki.pack()
Label(master,text='Podaj link do filmu: ',font=mojfont).place(x=0,y=0)
def akcja():
    link = linki.get()
    try:
        if Moj_YouTube.Start(link) == None:
            yt = YouTube(link)
            tytul = Moj_YouTube(yt).tytul
            autor = Moj_YouTube(yt).autor
            wyswietlenia = Moj_YouTube(yt).wyswietlenia
            if len(tytul) > 42:
                tytul = tytul[:42]
                tytul += '(...)' 
            tytul1 = Label(master,text=f'Tytuł  =  {tytul}                                               ',font=mojfont)
            tytul1.place(x=0,y=50)
            autor1 = Label(master,text=f"Autor  =  {autor}                                             ",font=mojfont)
            autor1.place(x=0,y=100)
            wyswietlenia1 = Label(master,text=f'Wyświetlenia  =  {wyswietlenia}                                       ',font=mojfont)
            wyswietlenia1.place(x=0,y=150)
            Label(master,text='Wybierz format filmu                ',font=mojfont).place(x=0,y=200)
            def mp3przycisk():
                tytul2 = simpledialog.askstring("Pobieranie",'Zapisz plik MP3 jako:')
                if '?' in tytul2 or tytul2[0] == '/' or '*' in tytul2 or ':' in tytul2 or '"' in tytul2 or '<' in tytul2 or '>' in tytul2 or tytul2[0] == "\\":
                    raise 'Niedozwolony znak w tytule'       
                Moj_YouTube.MP3(yt,tytul2=tytul2)
                Label(master,text='POBIERANIE UKOŃCZONE',font=pobieranie_font).place(x=0,y=200)
            def mp4przycisk():
                tytul2 = simpledialog.askstring("Pobieranie",'Zapisz plik MP4 jako:')
                if '?' in tytul2 or tytul2[0] == '/' or '*' in tytul2 or ':' in tytul2 or '"' in tytul2 or '<' in tytul2 or '>' in tytul2 or tytul2[0] == "\\":
                    raise 'Niedozwolony znak w tytule'     
                Moj_YouTube.MP4(yt,tytul2=tytul2)
                Label(master,text='POBIERANIE UKOŃCZONE',font=pobieranie_font).place(x=0,y=200)
            tkinter.Button(master,text='Pobierz w formacie MP3',command=mp3przycisk).place(x=400,y=150)
            tkinter.Button(master,text='Pobierz w formacie MP4',command=mp4przycisk).place(x=400,y=200)
            
        else:
               Label(master,text='film jest niedostępny',font=mojfont).place(x=0,y=200)  
    except:
        Label(master,text='błędny link lub błąd połączenia             ',font=mojfont).place(x=0,y=200)
tkinter.Button(master,text="Szukaj",command=akcja).pack()
master.mainloop()
