from email import message
import imp
from multiprocessing.dummy import Process
from pprint import pprint
from turtle import update
import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.graphics import *
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
import connector
import speech
import threading
from TikTokLive import TikTokLiveClient
from time import sleep

client = TikTokLiveClient(unique_id="@mystique_jerseys", process_initial_data=False)

class ChatLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MyLayout(FloatLayout):
    def do_layout(self, *args, **kwargs):
        super(MyLayout, self).do_layout()
        width, height = Window.size
        if width < 607:
            Window.size = 607, Window.size[1]
    pass

class MyApp(App):
    Window.minimum_width = 608
    def loop(self):
        print('width: ' + str(Window.size[0]))
        print('height: ' + str(Window.size[1]))
    def update_chat(comment):
        print(comment + "\n")
    def stop(self, *largs):
        global speech_read
        connector.stop = True
        client.loop.stop()
        thread1.join()
        print("thread1 stopped\n")
        speech.read = False
        thread2.join()
        print("thread2 stopped\n")
    def build(self):
        thread1.start()
        thread2.start()
        connector.curr_app = MyLayout()
        return connector.curr_app

if __name__ == '__main__':
    speech.read = True
    thread1 = threading.Thread(target=connector.main)
    thread2 = threading.Thread(target=speech.main)
    MyApp().run()