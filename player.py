# Libraries Used
# Pygame: to play, pause, load, stop, and resume music.
# Tkinter: to develop GUI.
# os: to access the song folder.
# Functions Used
# play: It loads the active song from the list and plays the required song. It gets executed when the user clicks on “play".
# pause: It pauses the required song. It gets executed when the user clicks on “pause".
# stop: It stops the required song. It gets executed when the user clicks on “stop".
# resume: It resumes the required song. It gets executed when the user clicks on “resume".
# Variables Used
# root: the main GUI window.
# songstatus: it stores the status of the currently active song.
# playlist: It stores the name of all songs available at the specified location.

import pygame #used to create video games
import tkinter as tkr #used to develop GUI
from tkinter.filedialog import askdirectory #it permit to select dir
import os #it permits to interact with the operating system

music_player = tkr.Tk() 
music_player.title("Music Player")
music_player.geometry("500x350")

directory = askdirectory()
os.chdir(directory) #it permits to chenge the current dir
song_list = os.listdir() #it returns the list of files song

play_list = tkr.Listbox(music_player, font="Ubuntu 12 bold", bg="yellow", selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1


pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def pause():
    pygame.mixer.music.pause()
def resume():
    pygame.mixer.music.unpause()
def stop():
    pygame.mixer.music.stop()


button1 = tkr.button(music_player, width=2, height=2, font="Ubuntu 12 bold", text="PLAY", command=play, bg="green", fg="white")
button2 = tkr.button(music_player, width=5, height=3, font="Ubuntu 12 bold", text="PAUSE", command=pause, bg="blue", fg="white")
button3 = tkr.button(music_player, width=5, height=3, font="Ubuntu 12 bold", text="RESUME", command=resume, bg="orange", fg="white")
button4 = tkr.button(music_player, width=5, height=3, font="Ubuntu 12 bold", text="STOP", command=stop, bg="red", fg="white")


var = tkr.StringVar() 
song_title = tkr.Label(music_player, font="Ubuntu 12 bold", textvariable=var)

song_title.pack()
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
play_list.pack(fill="both", expand="yes")
music_player.mainloop()
