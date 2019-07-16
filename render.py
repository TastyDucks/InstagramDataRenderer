# Created by TastyDucks, 2019-03-23

#
# Imports.
#

# Standard libraries.

import base64
import json
import os
from shutil import rmtree
import sys
import time
import zipfile

# Other libraries.

import requests

# Custom libraries.

import templates

#
# Functions.
#

def Log(Message, LogLevel=0):
    """
    Logs a message according to its LogLevel.
    Logged messages are printed in stdout and are saved in a file named "log.txt".
    """
    if Message is None:
        raise ValueError("Log message has no value.")
    elif LogLevel == 0:
        LogLevel = "INFO"
    elif LogLevel == 1:
        LogLevel = "WARN"
    else:
        LogLevel = "FAIL"
    Time = time.strftime("%Y-%m-%d %H:%M:%S")
    Message = f"[{Time}] [{LogLevel}] {Message}"
    print(Message)
    try:
        with open("IDR.log", "a+", encoding="utf8") as File:
            File.write(Message + "\n")
    except OSError:
        raise OSError("Unable to write to log file.")

#
# Body.
#

if len(sys.argv) < 2:
    Log("No archive file specified. Syntax is \"python render.py FILENAME\".", 1)
    sys.exit()

StartTime = time.perf_counter()

# Extract archive.

with zipfile.ZipFile(sys.argv[-1], "r") as Zip:
    Zip.extractall(".Archive")
Log("Archive extracted.")

# Create output directory.

if not os.path.exists("Render"):
    os.mkdir("Render")

# Render CSS file.
with open("Render/style.css", "w+") as File:
    File.write(templates.CSS)
Log("CSS rendered.")

# Render comments on posts.

# TODO (Might require online lookup; provided data is just a timestamp and username.)
Log("Skipping comments...", 1)

# Render liked comments on posts.

# TODO (Perhaps combine with above?)
Log("Skipping liked comments...", 1)

# Render liked posts.

# TODO (Might require online lookup; provided data is just a timestamp and username.)
Log("Skipping liked posts...", 1)

# Render direct messages.

with open(".Archive/messages.json", "r") as File:
    Direct = json.load(File)

ConversationNumber = 0
DirectBody = ""
Conversations = ""

for Conversation in Direct:
    ConversationBody = ""
    Users = ""
    Messages = ""
    ConversationNumber += 1
    MessageNumber = 0
    MemberMessageCounts = {}
    Log(f"Rendering Conversation {ConversationNumber} / {len(Direct)}...")
    Members = Conversation["participants"]
    ConversationContent = Conversation["conversation"]
    ConversationContent.reverse()
    try:
        TotalMessages = len(ConversationContent)
    except:
        TotalMessages = 1
        Log("A conversation has no content?", 1)
        try:
            print(str(ConversationContent))
        except:
            # Do nothing lol
            print("\nlol\n")
    for Message in ConversationContent:
        MessageNumber += 1
        PercentComplete = str(round(MessageNumber / TotalMessages * 100))
        print(f"Message {MessageNumber} / {TotalMessages}: {PercentComplete}%", end='\r')
        Username = Message["sender"]
        MemberMessageCounts[Username] = MemberMessageCounts.setdefault(Username, 0) + 1
        Timestamp = Message["created_at"]
        if "likes" in Message: # Process likes if any exist. Otherwise return null.
            Usernames = []
            Likes = Message["likes"]
            for Like in Likes:
                Usernames.append(Like["username"])
            Usernames = ", ".join(Usernames)
            Likes = templates.DirectMessageLikes.format(Usernames=Usernames)
        else:
            Likes = ""
        if "text" in Message: # Process text content if it exists.
            Content = Message["text"]
            DM = templates.DirectMessage.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
        elif "media" in Message: # Process media content if it exists.
            URL = Message["media"]
            Content = bytearray()
            Response = requests.get(URL, stream=True)
            Length = Response.headers.get("content-length")
            DL = 0
            Length = int(Length)
            for Data in Response.iter_content(chunk_size=4096):
                DL += len(Data)
                Content.extend(Data)
                Done = int(100 * DL / Length)
                # print(f"{DL} / {Length} KB: {Done}%", end="\r")
            Content = str(base64.b64encode(Content).decode("utf8"))
            if ".jpg" in URL:
                DM = templates.DirectMessageImage.format(Timestamp=Timestamp,Username=Username,Base64Data=Content,Likes=Likes)
            elif ".mp4" in URL:
                DM = templates.DirectMessageVideo.format(Timestamp=Timestamp,Username=Username,Base64Data=Content,Likes=Likes)
            else:
                Content = "ERROR PROCESSING MEDIA AT URL: {URL}"
        else:
            Content = "UNSUPPORTED MESSAGE FORMAT"
            DM = templates.DirectMessage.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
        Messages += DM + "\r\n"
    for Member in MemberMessageCounts:
        NumberOfMessages = MemberMessageCounts[Member]
        PercentOfMessages = str(round((NumberOfMessages / TotalMessages) * 100, 2))
        UserEntry = templates.DirectParticipant.format(Name=Member,NumberOfMessages=NumberOfMessages,PercentOfMessages=PercentOfMessages)
        Users += UserEntry + "\r\n"
    ConversationBody = templates.ConversationBody.format(ConversationNumber=ConversationNumber,TotalMessages=str(TotalMessages),Users=Users,Messages=Messages)
    with open(".Conversations.tmp", "a+") as File: # Write each conversation to disk once we are finished rendering it to preserve system memory. TODO: Don't write to an intermediate file; write directly to "messages.html"
        File.write(ConversationBody + "\r\n")

with open(".Conversations.tmp", "r") as File:
    Conversations = File.read()

DirectBody += templates.DirectBody.format(Conversations=Conversations)

Log("Writing data to file...")
with open("Render/messages.html", "w+") as File:
    File.write(DirectBody)
Log("Direct messages rendered.", 0)

# Render posts.

# TODO
Log("Skipping user posts...", 1)

# Render profile.

# TODO
Log("Skipping profile...", 1)

# Render saved posts.

# TODO (Might require online lookup; provided data is just a timestamp and username.)
Log("Skipping saved posts...", 1)

# Render stories.

# TODO
Log("Skipping user stories...", 1)

# Render story interactions.

# TODO (Might require online lookup; provided data is just a timestamp and username.)
Log("Skipping story interactions...", 1)

# Render index.

with open("Render/index.html", "w+") as File:
    File.write(templates.Index)
Log("Index rendered.")

# Clean up files.

os.remove(".Conversations.tmp")
rmtree(".Archive")
Log("Temporary files deleted.")

# Finish execution.

StopTime = time.perf_counter()
Log(f"Rendering completed in {round(StopTime - StartTime, 2)} seconds.")