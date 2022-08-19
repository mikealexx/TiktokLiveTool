import multiprocessing
from bidi.algorithm import get_display
import asyncio
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import *
from TikTokLive.types.errors import *
import os
import sys
import subprocess
import time
import gui
import speech

client = gui.client

curr_app = None

stop = False

@client.on("comment")
async def on_connect(event: CommentEvent):
    try:
        speech.curr_comment = event.comment
    except UnicodeEncodeError:
        speech.curr_comment = ''
    curr_app.ids.chat_history.text += ("[color=#04d3ff]" + event.user.nickname + " said:\n    " + "[/color]" + event.comment + "\n")
    if(stop):
        return None
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)

def main():
    try:
        client.run()
    except FailedConnection:
        print("LIVE SESSION OFFLINE")
    except KeyboardInterrupt:
        print("GOOD BYE BITCH")