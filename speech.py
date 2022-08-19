from time import sleep
import pyttsx3
import gui

engine = pyttsx3.init()
global last_comment
global curr_comment
global read

def main():
    global last_comment
    global curr_comment
    global read
    curr_comment = ''
    while(read):
        try:
            engine.say(curr_comment)
            engine.runAndWait()
            last_comment = curr_comment
        except KeyboardInterrupt:
            break
        if read == False:
            return None
    curr_comment = ''
    return None
