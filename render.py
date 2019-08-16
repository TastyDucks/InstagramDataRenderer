#
# Imports.
#

# Standard libraries.

import base64
import collections
import json
import os
import re
from shutil import rmtree
from signal import signal, SIGINT
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

def CurrentTime():
    """
    Returns the current time as a string formatted YYYY-MM-DD HH:MM:SS.
    """
    return time.strftime("%Y-%m-%d %H:%M:%S")

def Download(URL):
    """
    Downloads a file from a URL and returns its base64 data as a string.
    """
    Content = bytearray()
    try:
        Response = requests.get(URL, stream=True)
    except:
        Response = None # This probably will occur when the URL is listed as "Media share unavailable".
    if not Response:
        return False, templates.Image404 # If any HTTP error occurs we just use the 404 image.
    Length = Response.headers.get("content-length")
    DL = 0
    Length = int(Length)
    for Data in Response.iter_content(chunk_size=4096):
        DL += len(Data)
        Content.extend(Data)
        Done = int(100 * DL / Length)
        if Length >= 10000000: # Display a progress counter for download if the resource size is greater than 10 MB.
            print(f"{DL} / {Length} KB: {Done}%", end="\r")
    return True, str(base64.b64encode(Content).decode("utf8"))

def Exit():
    """
    Exit.
    """
    Log("Stopped.")
    #sys.exit()
    os._exit(0) # TODO: Might be a bad way to exit. Consider replacing.

def FormatText(Text):
    """
    Adds HTML links to any Instagram accounts, hashtags, or URLs in a text string. Also replaces newlines with "<br>".
    """
    Text = str(Text)
    Text = re.sub(r"https?:\/\/\S+", lambda match: '<a href=\"{0}\">{0}</a>'.format(match.group()), Text) # Add HTML links to web addresses.
    Text = re.sub(r"@\S+", lambda match: '<a href=\"https://www.instagram.com/{0}\">@{0}</a>'.format(match.group()[1:]), Text) # Add HTML links to user accounts.
    Text = re.sub(r"#\S+", lambda match: '<a href=\"https://www.instagram.com/explore/tags/{0}">#{0}</a>'.format(match.group()[1:]), Text) # Add HTML links to hashtags.
    Text = re.sub("\\n", "<br>", Text) # Replace "\n" with "<br>".
    return Text

def Log(Message, LogLevel=0):
    """
    Logs a message according to its LogLevel. Logged messages are printed in stdout and are saved in a file named "log.txt".
    """
    if Message is None:
        raise ValueError("Log message has no value.")
    elif LogLevel == 0:
        LogLevel = "INFO"
    elif LogLevel == 1:
        LogLevel = "WARN"
    else:
        LogLevel = "FAIL"
    Time = CurrentTime()
    Message = f"[{Time}] [{LogLevel}] {Message}"
    print(Message)
    try:
        with open("IDR.log", "a+", encoding="utf8") as File:
            File.write(Message + "\n")
    except OSError:
        raise OSError("Unable to write to log file.")

def SIGINTHandler(signal_received, frame):
    Log("SIGINT detected.", 1)
    Exit()

#
# Body.
#

signal(SIGINT, SIGINTHandler) # Register handler for ctrl+c.

StartTime = time.perf_counter()

Log("Started.")

# Parse arguments.

if sys.argv[-1] in ("--no-media", "-n"):
    NoMedia = True
    Log("Running in NoMedia mode. Rendered output for direct messages will be text only.", 1)
    Archives = sys.argv[1:-1]
else:
    NoMedia = False
    Archives = sys.argv[1:]

if len(Archives) < 1:
    Log("No archive files passed.", 2)
    Exit()

# Extract archive.

try:
    Path = Archives[0]
    with zipfile.ZipFile(Path, "r") as Zip: # Basic data and user media.
        Zip.extractall(".Archive")
    if len(Archives) > 1: # 2 archives.
        Path = sys.argv[2]
        with zipfile.ZipFile(Path, "r") as Zip: # Part two of ?: User media.
            Zip.extractall(".Archive")
    if len(Archives) > 2: # 3 archives.
        with open(".Archive/media.json", "r") as File:
            Media1 = json.load(File)
        Path = sys.argv[3]
        with zipfile.ZipFile(Path, "r") as Zip: # Part three of ?: User media.
            Zip.extractall(".Archive")
        with open(".Archive/media.json", "r") as File:
            Media2 = json.load(File)
        Media = {**Media1, **Media2} # Concatenate media.json files.
        with open(".Archive/media.json", "w+") as File:
            json.dump(Media, File)
except FileNotFoundError:
    Log(f"File not found: \"{Path}\"", 2)
    Exit()

Log("Archive(s) extracted.")

# Create output directory.

if not os.path.exists("Render"):
    os.mkdir("Render")

# Render CSS file.
with open("Render/style.css", "w+", encoding="utf8") as File:
    File.write(templates.CSS)
Log("CSS rendered.")

# Render comments on posts.

Log("Skipping comments: No context.", 1) # TODO: This might be possible with online lookup; provided data is just a timestamp and username.

# Render liked comments on posts.

Log("Skipping liked comments: No data.", 1) # TODO: No information is provided on this.

# Render liked posts.

Log("Skipping liked posts: No context.", 1) # TODO: This might be possible with online lookup; provided data is just a timestamp and username.

# Render direct messages.

with open(".Archive/messages.json", "r") as File:
    Direct = json.load(File)

ConversationNumber = 0
ConversationIndexBody = ""
Conversations = {}

for Conversation in Direct:
    ConversationName = ""
    ConversationBody = ""
    Users = ""
    Messages = ""
    ConversationNumber += 1
    MessageNumber = 0
    MemberMessageCounts = {}
    Log(f"Rendering Conversation {ConversationNumber} / {len(Direct)}")
    Members = Conversation["participants"]
    ConversationContent = Conversation["conversation"]
    ConversationContent.reverse()
    try:
        TotalMessages = len(ConversationContent)
    except:
        TotalMessages = 1
        Log("A conversation has no content?", 1)
        print(str(ConversationContent))
    for Message in ConversationContent:
        MessageNumber += 1
        PercentComplete = str(round(MessageNumber / TotalMessages * 100))
        print(f"Message {MessageNumber} / {TotalMessages}: {PercentComplete}%", end='\r')
        Username = Message["sender"]
        MemberMessageCounts[Username] = MemberMessageCounts.setdefault(Username, 0) + 1
        OriginalTimestamp = Message["created_at"] # The original un-altered timestamp of the message is preserved so that it can be looked up in the data files if an error occurs.
        Timestamp = OriginalTimestamp.replace("T", " ").split("+")[0] # Replace the "T" in the timestamp with a space and remove the UTC offset.
        if "likes" in Message: # Process likes if any exist. Otherwise return null.
            Usernames = []
            Likes = Message["likes"]
            for Like in Likes:
                Usernames.append(Like["username"])
            Usernames = ", ".join(Usernames)
            Likes = templates.DirectMessageLikes.format(Usernames=Usernames)
        else:
            Likes = ""
        if "story_share" in Message: # Process shared stories.
            Content = FormatText(Message["story_share"])
            DM = templates.DirectMessageStory.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
            Content = FormatText(Message["text"])
            if Content:
                DM = DM + "\r\n" + templates.DirectMessage.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
        elif "text" in Message: # Process text content. (This is after "story_share" because that can also have a "text" component.)
            Content = FormatText(Message["text"])
            DM = templates.DirectMessage.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
        elif "heart" in Message: # Process "heart" content.
            Content = Message["heart"]
            DM = templates.DirectMessage.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
        elif "media" in Message: # Process media content. # TODO: Consolidate this code. Nearly the same thing is duplicated three times here.
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
                        Log(f"Unsupported message format: unknown media type: {OriginalTimestamp}", 2)
                else:
                    if not "Media share unavailable" in URL: # If the resource is explicitly nonexistant, we don't log the error.
                        Log(f"Unable to download resource: {OriginalTimestamp}", 1)
                    DM = templates.DirectMessageImage.format(Timestamp=Timestamp,Username=Username,Base64Data=Content,Likes=Likes)
            else:
                DM = ""
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
                        Log(f"Unsupported message format: unknown media type: {OriginalTimestamp}", 2)
                else:
                    if not "Media share unavailable" in URL: # If the resource is explicitly nonexistant, we don't log the error.
                        Log(f"Unable to download resource: {OriginalTimestamp}", 1)
                    DM = templates.DirectMessageImage.format(Timestamp=Timestamp,Username=Username,Base64Data=Content,Likes=Likes)
            else:
                DM = ""
        elif "media_share_url" in Message: # Process shared posts.
            if not NoMedia:
                URL = Message["media_share_url"]
                PostOwner = Message["media_owner"]
                Caption = FormatText(Message["media_share_caption"])
                Reply, Content = Download(URL)
                if Reply:
                    if ".jpg" in URL:
                        DM = templates.DirectMessagePostImage.format(Timestamp=Timestamp,Username=Username,PostOwner=PostOwner,Caption=Caption,Base64Data=Content,Likes=Likes)
                    elif ".mp4" in URL:
                        DM = templates.DirectMessagePostVideo.format(Timestamp=Timestamp,Username=Username,PostOwner=PostOwner,Caption=Caption,Base64Data=Content,Likes=Likes)
                    else:
                        Content = "UNSUPPORTED MESSAGE FORMAT: UNKNOWN MEDIA TYPE"
                        DM = templates.DirectMessage.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
                        Log(f"Unsupported message format: unknown media type: {OriginalTimestamp}", 2)
                else:
                    if not "Media share unavailable" in URL: # If the resource is explicitly nonexistant, we don't log the error.
                        Log(f"Unable to download resource: {OriginalTimestamp}", 1)
                    DM = templates.DirectMessagePostImage.format(Timestamp=Timestamp,Username=Username,PostOwner=PostOwner,Caption=Caption,Base64Data=Content,Likes=Likes)
            else:
                DM = ""
        elif "video_call_action" in Message: # Process video call actions.
            Content = Message["video_call_action"]
            DM = templates.DirectMessageVideoCallAction.format(Timestamp=Timestamp,Username=Username,Content=Content)
        elif "profile_share_username" in Message: # Process shared profiles.
            ProfileUsername = Message["profile_share_username"]
            DM = templates.DirectMessageProfile.format(Timestamp=Timestamp,Username=Username,ProfileUsername=ProfileUsername)
        elif "action" in Message: # Process group actions, including changing the name of the group.
            Content = Message["action"]
            if " named the group " in Content: # Extract the groups name, if one exists.
                ConversationName = Content.split(" named the group ",1)[1]
            DM = templates.DirectMessageGroupAction.format(Timestamp=Timestamp,Username=Username,Content=Content)
        elif "voice_media" in Message: # Process voice media.
            if not NoMedia:
                Content = "UNSUPPORTED MESSAGE FORMAT: VOICE MEDIA"
                DM = templates.DirectMessage.format(Timestamp=Timestamp,Username=Username,Content=Content,Likes=Likes)
                Log(f"Unsupported message format: voice media: {OriginalTimestamp}", 1)
        elif "animated_media_images" in Message: # Process GIPHY media.
            if not NoMedia:
                Reply, Content = Download(Message["animated_media_images"]["original"]["mp4"])
                if Reply:
                    DM = templates.DirectMessageGIPHY.format(Timestamp=Timestamp,Username=Username,Base64Data=Content,Likes=Likes)
                else:
                    Log(f"Unable to download resource: {OriginalTimestamp}", 1)
                    DM = templates.DirectMessageImage.format(Timestamp=Timestamp,Username=Username,Base64Data=Content,Likes=Likes)
            else:
                DM = ""
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
            Log(f"Unsupported message format: unknown: {OriginalTimestamp}", 2)
        Messages += DM + "\r\n"
    MemberMessageCounts = collections.OrderedDict(sorted(MemberMessageCounts.items()))
    for Member in MemberMessageCounts:
        NumberOfMessages = MemberMessageCounts[Member]
        PercentOfMessages = str(round((NumberOfMessages / TotalMessages) * 100, 2))
        UserEntry = templates.DirectParticipant.format(Username=Member,NumberOfMessages=NumberOfMessages,PercentOfMessages=PercentOfMessages)
        Users += UserEntry + "\r\n"
    if ConversationName != "":
        ConversationName = ": " + ConversationName
    Conversations[ConversationNumber] = ConversationName
    PrologueHTML = templates.PrologueHTML.format(Time=CurrentTime())
    ConversationBody = templates.ConversationBody.format(PrologueHTML=PrologueHTML,ConversationNumber=ConversationNumber,ConversationName=ConversationName,TotalMessages=str(TotalMessages),Users=Users,Messages=Messages)
    with open(f"Render/conversation{ConversationNumber}.html", "w+", encoding="utf8") as File: # Write each conversation to disk once we are finished rendering it.
        File.write(ConversationBody)

ConversationIndex = ""
for Conversation in Conversations:
    if Conversations[Conversation] != "":
        ConversationName = Conversations[Conversation]
    else:
        ConversationName = ""
    Entry = templates.ConversationIndexEntry.format(Conversation=Conversation,ConversationName=ConversationName)
    ConversationIndex += Entry

PrologueHTML = templates.PrologueHTML.format(Time=CurrentTime())
ConversationIndexBody += templates.ConversationIndexBody.format(PrologueHTML=PrologueHTML,ConversationIndex=ConversationIndex)

with open("Render/messages.html", "w+", encoding="utf8") as File:
    File.write(ConversationIndexBody)
Log("Direct messages rendered.")

# Render posts.

with open(".Archive/media.json", "r") as File:
    Media = json.load(File)
Stories, Photos, Videos, Direct = Media["stories"], Media["photos"], Media["videos"], Media["direct"]
Posts = Photos + Videos
Posts = sorted(Posts, key = lambda x: x["taken_at"])
RenderedPosts = ""
NumberOfPosts = len(Posts)
CurrentPost = 0
for Post in Posts:
    CurrentPost += 1
    Done = int(100 * CurrentPost / NumberOfPosts)
    print(f"Rendered {CurrentPost} / {NumberOfPosts} posts: {Done}%", end='\r')
    Caption = FormatText(Post["caption"])
    Path = Post["path"]
    OriginalTimestamp = Post["taken_at"]
    Timestamp = OriginalTimestamp.replace("T", " ") # Replace the "T" in the timestamp with a space.
    try:
        Location = Post["location"]
    except:
        Location = ""
    try:
        with open(f".Archive/{Path}", "rb") as File:
            Content = base64.b64encode(File.read()).decode("utf8")
            if ".mp4" in Path:
                Post = templates.PostVideo.format(Timestamp=Timestamp,Caption=Caption,Base64Data=Content)
            elif ".jpg" in Path:
                Post = templates.PostImage.format(Timestamp=Timestamp,Caption=Caption,Base64Data=Content)
            else:
                Caption = "UNSUPPORTED POST FORMAT: UNKNOWN MEDIA TYPE"
                Content = templates.Image404
                Post = templates.PostImage.format(Timestamp=Timestamp,Caption=Caption,Base64Data=Content)
                Log(f"Unsupported post format: unknown media type: {OriginalTimestamp}", 2)
    except FileNotFoundError:
        Log(f"Unable to locate local resource: Post: {OriginalTimestamp}", 1)
        Content = templates.Image404
        Post = templates.PostImage.format(Timestamp=Timestamp,Caption=Caption,Base64Data=Content)
    RenderedPosts += Post + "\r\n"

PrologueHTML = templates.PrologueHTML.format(Time=CurrentTime())
PostsBody = templates.PostsBody.format(PrologueHTML=PrologueHTML,NumberOfPosts=NumberOfPosts,Posts=RenderedPosts)

with open("Render/posts.html", "w+", encoding="utf8") as File:
    File.write(PostsBody)

Log("Posts rendered.")

# Render profile.

with open(".Archive/profile.json", "r") as File:
    Profile = json.load(File)
Biography, JoinDate, Email, Gender, PrivateAccount, URL, Username, BusinessCategory, BusinessEmail = FormatText(Profile["biography"]), Profile["date_joined"].replace("T", " "), Profile["email"], str(Profile["gender"]), Profile["private_account"], Profile["profile_pic_url"], Profile["username"], Profile["business_category"], Profile["business_email"]
Reply, Content = Download(URL)
if not Reply:
    Log("Unable to download resource: profile_pic_url", 1)

PrologueHTML = templates.PrologueHTML.format(Time=CurrentTime())
ProfileBody = templates.ProfileBody.format(PrologueHTML=PrologueHTML,Username=Username,Base64Data=Content,Biography=Biography,Gender=Gender,JoinDate=JoinDate,Email=Email,PrivateAccount=PrivateAccount,BusinessCategory=BusinessCategory,BusinessEmail=BusinessEmail)

with open("Render/profile.html", "w+", encoding="utf8") as File:
    File.write(ProfileBody)

# Render saved posts.

Log("Skipping saved posts: No context.", 1)  # TODO: This might be possible with online lookup; provided data is just a timestamp and username.

# Render stories.

RenderedStories = ""
NumberOfStories = len(Stories)
CurrentStory = 0
Stories.reverse() # We reverse this list because we want the oldest stories to come first on the page.
for Story in Stories:
    CurrentStory += 1
    Done = int(100 * CurrentStory / NumberOfStories)
    print(f"Rendered {CurrentStory} / {NumberOfStories} stories: {Done}%", end='\r')
    Caption = FormatText(Story["caption"])
    Path = Story["path"]
    OriginalTimestamp = Story["taken_at"]
    Timestamp = OriginalTimestamp.replace("T", " ")
    with open(f".Archive/{Path}", "rb") as File:
        Content = base64.b64encode(File.read()).decode("utf8")
    if ".jpg" in Path:
        Story = templates.StoryImage.format(Timestamp=Timestamp,Caption=Caption,Base64Data=Content)
    else:
        Caption = "UNSUPPORTED STORY FORMAT: UNKNOWN MEDIA TYPE"
        Content = templates.Image404
        Story = templates.PostImage.format(Timestamp=Timestamp,Caption=Caption,Base64Data=Content)
        Log(f"Unsupported story format: unknown media type: {OriginalTimestamp}", 2)
    RenderedStories += Story + "\r\n"

PrologueHTML = templates.PrologueHTML.format(Time=CurrentTime())
StoriesBody = templates.StoriesBody.format(PrologueHTML=PrologueHTML,NumberOfStories=NumberOfStories,Stories=RenderedStories)

with open("Render/stories.html", "w+", encoding="utf8") as File:
    File.write(StoriesBody)

Log("Stories rendered.")

# Render story interactions.

Log("Skipping story interactions: No context.", 1)  # TODO: This might be possible with online lookup; provided data is just a timestamp and username.

# Render index.

with open("Render/index.html", "w+", encoding="utf8") as File:
    File.write(templates.Index)
Log("Index rendered.")

# Clean up files.

rmtree(".Archive")
Log("Temporary files deleted.")

# Finish execution.

StopTime = time.perf_counter()
Log(f"Rendering completed in ~{round(StopTime - StartTime, 2)} seconds.")
Exit()