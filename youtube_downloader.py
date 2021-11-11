from pytube import YouTube
from moviepy.editor import *
import os
import sys

class Moj_YouTube:
    def __init__(self,yt):
        self.tytul = yt.title
        self.autor = yt.author
        self.wyswietlenia = yt.views
    
    def MP4(self,yt):
        pobier = yt.streams.get_highest_resolution()
        pobier.download()
    
    def MP3(self,yt):    
        pobierz = yt.streams.get_lowest_resolution()
        pobierz.download()
        video = VideoFileClip(os.path.join(f"{yt.title}.mp4"))
        video.audio.write_audiofile(os.path.join(f"{yt.title}.mp3"))
        video.close()
        os.remove(f"{yt.title}.mp4")
        
    def Start(link):

            try:
                yt = YouTube(link)
            except:
                print("Błędny link, spróbuj ponownie")
                input()
                sys.exit()
            zgadza_sie = yt.check_availability()
            if zgadza_sie != None:
                print("Film jest niedostępny")
                input()
                sys.exit()


#Wykonali: Maksym Bernasiewicz, Piotr Suchomski, Mateusz Mercik, Adrian Kowalewski
    