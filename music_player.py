import pygame
import tkinter as tk
from tkinter import filedialog

pygame.mixer.init()

def load_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

root = tk.Tk()
root.title("Simple Music Player")

load_button = tk.Button(root, text="Load Music", command=load_music)
load_button.grid(row=0, column=0, padx=10, pady=10)

play_button = tk.Button(root, text="Play", command=unpause_music)
play_button.grid(row=1, column=0, padx=10, pady=10)

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.grid(row=2, column=0, padx=10, pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()
