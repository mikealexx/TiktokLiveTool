from time import sleep
import pyttsx3
import gui

engine = pyttsx3.init()
global speech_read

def main():
    global speech_read
    speech_read = True
    last_comment = ""
    curr_comment = ""
    while(True):
        try:
            with open("curr_comment.txt", "r") as file:
                curr_comment = file.read().strip()
                if last_comment != curr_comment:
                    engine.say(curr_comment)
                    engine.runAndWait()
                    last_comment = curr_comment
        except KeyboardInterrupt:
            break
        if(speech_read == False):
            return None
