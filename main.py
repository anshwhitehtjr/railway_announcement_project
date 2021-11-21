# region namespaces
import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

# endregion

# region LOGIC
def testToSpeech(text, filename):
    pass


def mergeAudios(audios):
    pass


def generateSkeleton():
    audio = AudioSegment.from_mp3("railway.mp3")
    # Generate "Kripya Dhan de"
    start = 
    finish = 
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3")

def generateAnnouncement(filename):
    pass


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcements...")
    generateAnnouncement("announce_hindi.xlsx")

# endregion
