# This program uses the pyttsx3 library to convert text into speech.
# It iterates through a list of names and speaks each one aloud.


import pyttsx3

names = ["Alice", "Bob", "Charlie", "Diana"]

for name in names:
    print(f"Speaking: {name}")
    engine = pyttsx3.init()     # Re-initialize engine per name
    engine.say(name)
    engine.runAndWait()
    engine.stop()               # Clean up after speaking
