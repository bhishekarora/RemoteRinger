#!/usr/bin/python
import sys
from flask import Flask
import threading
import pygame

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
print(f"Python path: {sys.path}")

app = Flask(__name__)
pygame.mixer.init()

def play_sound():
    try:
        pygame.mixer.music.load('bell.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error playing sound: {e}")

@app.route('/')
def index():
    threading.Thread(target=play_sound).start()
    return 'Bell rung!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)