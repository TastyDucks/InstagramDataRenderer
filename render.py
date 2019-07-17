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

def Download(URL):
    """
    Downloads a file from a URL and returns its base64 data as a string.
    """
    Content = bytearray()
    try:
        Response = requests.get(URL, stream=True)
    except:
        Response = None # This probably will occur when the URL is listed as "Media share unavaliable"
    if not Response:
        return False, templates.Image404 # If any HTTP error occurs we just use the 404 image.
    Length = Response.headers.get("content-length")
    DL = 0
    Length = int(Length)
    for Data in Response.iter_content(chunk_size=4096):
        DL += len(Data)
        Content.extend(Data)
        Done = int(100 * DL / Length)
        # print(f"{DL} / {Length} KB: {Done}%", end="\r")
    return True, str(base64.b64encode(Content).decode("utf8"))

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

if len(sys.argv) < 4:
    Log("Not enough archive files specified. Syntax is \"python render.py ARCHIVEPART1 ARCHIVEPART2 ARCHIVEPART3\".", 1)
    sys.exit()

StartTime = time.perf_counter()

if sys.argv[-1] == "--no-media":
    NoMedia = True
    Log("Running in NoMedia mode. Rendered output will be text only.", 1)
else:
    NoMedia = False

# Extract archive.

with zipfile.ZipFile(sys.argv[1], "r") as Zip: # Part one.
    Zip.extractall(".Archive")
with zipfile.ZipFile(sys.argv[2], "r") as Zip: # Part two.
    Zip.extractall(".Archive")
with zipfile.ZipFile(sys.argv[3], "r") as Zip: # Part three.
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
Conversations = {}

for Conversation in Direct:
    ConversationName = ""
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
        if "text" in Message: # Process text content.
            Content = Message["text"]
            DM = templates.DirectMessage.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
        elif "heart" in Message: # Process text content.
            Content = Message["heart"]
            DM = templates.DirectMessage.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
        elif "story_share" in Message: # Process shared stories
            Content = Message["story_share"]
            DM = templates.DirectMessageStory.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
        elif "media" in Message: # Process media content.
            if not NoMedia:
                URL = Message["media"]
                Reply, Content = Download(URL)
                if Reply:
                    if ".jpg" in URL:
                        DM = templates.DirectMessageImage.format(Timestamp=Timestamp,Username=Username,Base64Data=Content,Likes=Likes)
                    elif ".mp4" in URL:
                        DM = templates.DirectMessageVideo.format(Timestamp=Timestamp,Username=Username,Base64Data=Content,Likes=Likes)
                    else:
                        Content = "UNSUPPORTED MESSAGE FORMAT: UNKNOWN MEDIA TYPE"
                        DM = templates.DirectMessage.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
                        Log(f"Unsupported message format: unknown media type: {Timestamp}", 2)
                else:
                    if not "Media share unavailable" in URL: # If the resource is explicitly nonexistant, we don't log the error.
                        Log(f"Unable to download resource: {Timestamp}", 1)
                    DM = templates.DirectMessageImage.format(Timestamp=Timestamp,Username=Username,Base64Data=Content,Likes=Likes)
        elif "media_url" in Message: # Process media content.
            if not NoMedia:
                URL = Message["media_url"]
                Reply, Content = Download(URL)
                if Reply:
                    if ".jpg" in URL:
                        DM = templates.DirectMessageImage.format(Timestamp=Timestamp,Username=Username,Base64Data=Content,Likes=Likes)
                    elif ".mp4" in URL:
                        DM = templates.DirectMessageVideo.format(Timestamp=Timestamp,Username=Username,Base64Data=Content,Likes=Likes)
                    else:
                        Content = "UNSUPPORTED MESSAGE FORMAT: UNKNOWN MEDIA TYPE"
                        DM = templates.DirectMessage.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
                        Log(f"Unsupported message format: unknown media type: {Timestamp}", 2)
                else:
                    if not "Media share unavailable" in URL: # If the resource is explicitly nonexistant, we don't log the error.
                        Log(f"Unable to download resource: {Timestamp}", 1)
                    DM = templates.DirectMessageImage.format(Timestamp=Timestamp,Username=Username,Base64Data=Content,Likes=Likes)
        elif "media_share_url" in Message: # Process shared posts.
            if not NoMedia:
                URL = Message["media_share_url"]
                PostOwner = Message["media_owner"]
                Caption = Message["media_share_caption"]
                Reply, Content = Download(URL)
                if Reply:
                    if ".jpg" in URL:
                        DM = templates.DirectMessagePostImage.format(Timestamp=Timestamp,Username=Username,PostOwner=PostOwner,Caption=Caption,Base64Data=Content,Likes=Likes)
                    elif ".mp4" in URL:
                        DM = templates.DirectMessagePostVideo.format(Timestamp=Timestamp,Username=Username,PostOwner=PostOwner,Caption=Caption,Base64Data=Content,Likes=Likes)
                    else:
                        Content = "UNSUPPORTED MESSAGE FORMAT: UNKNOWN MEDIA TYPE"
                        DM = templates.DirectMessage.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
                        Log(f"Unsupported message format: unknown media type: {Timestamp}", 2)
                else:
                    if not "Media share unavailable" in URL: # If the resource is explicitly nonexistant, we don't log the error.
                        Log(f"Unable to download resource: {Timestamp}", 1)
                    DM = templates.DirectMessagePostImage.format(Timestamp=Timestamp,Username=Username,PostOwner=PostOwner,Caption=Caption,Base64Data=Content,Likes=Likes)
        elif "video_call_action" in Message: # Process video call actions.
            Content = Message["video_call_action"]
            DM = templates.DirectMessageVideoCallAction.format(Timestamp=Timestamp,Username=Username,Content=Content)
        elif "profile_share_username" in Message: # Process shared profiles.
            ProfileUsername = Message["profile_share_username"] # Formal username.
            ProfileShareName = Message["profile_share_name"]
            DM = templates.DirectMessageProfile.format(Timestamp=Timestamp,Username=Username,ProfileUsername=ProfileUsername,ProfileShareName=ProfileShareName)
        elif "action" in Message: # Process group actions, including changing the name of the group.
            Content = Message["action"]
            if " named the group " in Content: # Extract the groups name, if one exists.
                ConversationName = Content.split(" named the group ",1)[1]
            DM = templates.DirectMessageGroupAction.format(Timestamp=Timestamp,Username=Username,Content=Content)
        elif "voice_media" in Message: # Process voice media.
            if not NoMedia:
                Content = "UNSUPPORTED MESSAGE FORMAT: VOICE MEDIA"
                DM = templates.DirectMessage.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
                Log(f"Unsupported message format: voice media: {Timestamp}", 2)
        elif "animated_media_images" in Message: # Process GIPHY media.
            if not NoMedia:
                Reply, Content = Download(Message["animated_media_images"]["original"]["mp4"])
                if Reply:
                    DM = templates.DirectMessageGIPHY.format(Timestamp=Timestamp,Username=Username,Base64Data=Content,Likes=Likes)
                else:
                    Log(f"Unable to download resource: {Timestamp}", 1)
                    DM = templates.DirectMessageImage.format(Timestamp=Timestamp,Username=Username,Base64Data=Content,Likes=Likes)
        elif "location_name" in Message: # Process a location.
            LocationName = Message["location_name"]
            Address = Message["address"]
            City = Message["city"]
            Longitude = Message["longitude"]
            Latitude = Message["latitude"]
            DM = templates.DirectMessageLocation.format(Timestamp=Timestamp,Username=Username,LocationName=LocationName,Address=Address,City=City,Latitude=Latitude,Longitude=Longitude,Likes=Likes)
        elif "live_video_invite" in Message:
            DM = templates.DirectMessageLiveVideoInvite.format(Timestamp=Timestamp,Username=Username,Likes=Likes)
        elif "live_video_share" in Message:
            Content = Message["live_video_share"]
            DM = templates.DirectMessageLiveVideoShare.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
        else:
            Content = "UNSUPPORTED MESSAGE FORMAT: UNKNOWN"
            DM = templates.DirectMessage.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
            Log(f"Unsupported message format: unknown: {Timestamp}", 2)
        Messages += DM + "\r\n"
    for Member in MemberMessageCounts:
        NumberOfMessages = MemberMessageCounts[Member]
        PercentOfMessages = str(round((NumberOfMessages / TotalMessages) * 100, 2))
        UserEntry = templates.DirectParticipant.format(Username=Member,NumberOfMessages=NumberOfMessages,PercentOfMessages=PercentOfMessages)
        Users += UserEntry + "\r\n"
    if ConversationName != "":
        ConversationName = ": " + ConversationName
    Conversations[ConversationNumber] = ConversationName
    ConversationBody = templates.ConversationBody.format(ConversationNumber=ConversationNumber,ConversationName=ConversationName,TotalMessages=str(TotalMessages),Users=Users,Messages=Messages)
    with open(f"Render/conversation{ConversationNumber}.html", "w+") as File: # Write each conversation to disk once we are finished rendering it.
        File.write(ConversationBody)

ConversationIndex = ""
for Conversation in Conversations:
    if Conversations[Conversation] != "":
        ConversationName = Conversations[Conversation]
    else:
        ConversationName = ""
    Entry = f"<li><a href=\"conversation{Conversation}.html\">Conversation {Conversation}{ConversationName}</li></a>\r\n" # TODO: Make this located in templates.py
    ConversationIndex += Entry
DirectBody += templates.DirectBody.format(ConversationIndex=ConversationIndex)

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

rmtree(".Archive")
Log("Temporary files deleted.")

# Finish execution.

StopTime = time.perf_counter()
Log(f"Rendering completed in {round(StopTime - StartTime, 2)} seconds.")