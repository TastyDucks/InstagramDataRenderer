# Created by TastyDucks, 2019-03-23

#
# Imports.
#

# Standard libraries.

import json
import shutil
import sys
import tempfile
import time
import zipfile

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
    if LogLevel == 0:
        LogLevel = "INFO"
    else:
        LogLevel = "FAIL"
    Time = time.strftime("%Y-%m-%d %H:%M:%S")
    Message = f"[{Time}] [{LogLevel}] {Message}\r\n"
    print(Message)
    try:
        with open("log.txt", "a", encoding="utf8") as File:
            File.write(Message)
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

with zipfile.ZipFile(sys.argv[1], "r") as Zip:
    Zip.extractall("Archive")
Log("Archive extracted.")

# Render CSS file

# Render comments on posts.

# TODO (Might require online lookup; provided data is just a timestamp and username.)

# Render liked comments on posts.

# TODO (Perhaps combine with above?)

# Render liked posts.

# TODO (Might require online lookup; provided data is just a timestamp and username.)

# Render direct messages.

Direct = json.load("Archive/messages.json")


# Render posts.

# TODO

# Render profile.

# TODO

# Render saved posts.

# TODO (Might require online lookup; provided data is just a timestamp and username.)

# Render stories.

# TODO

# Render story interactions.

# TODO (Might require online lookup; provided data is just a timestamp and username.)

# Render index.

with open("index.html", "w+") as File:
    File.write(templates.Index)
Log("Index rendered.")

# Clean up files.

