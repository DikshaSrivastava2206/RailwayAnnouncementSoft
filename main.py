from email.mime import audio
import os
from tracemalloc import start
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):
    pass

def mergeAudios(audios):
    pass

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 88000 
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

def generateAnnouncement(filename):
    pass

if __name__=="__main__":
    print("Generate Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
