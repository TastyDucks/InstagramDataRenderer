# InstagramDataRenderer
A tool to render the data downloads provided by Instagram into user-friendly HTML documents for archival purposes.

Requirements:
 - [Python 3.6+](https://www.python.org/downloads/)
 - [Requests](https://2.python-requests.org/en/master/)

Usage: `python render.py FILENAME`

The main file to open in your browser is the index, `index.html`.

All remote resources are embedded in the generated html files — therefore, you will not need to rely on external CDNs to view your data in the future.

The font used is [Montserrat](https://fonts.google.com/specimen/Montserrat), as I believe this is a good free imitation of Instagram's default web font [Proxima Nova](https://fonts.adobe.com/fonts/proxima-nova).

## A few issues...

 - The CSS used isn't that great. Any commits regarding that are greatly appreciated!
 - At the moment, Instagram's data downloads do not provide adequate information for dealing with users who have changed their name. Because of this, direct messages you have with them may be split into two separate conversations.
 - Much of the context regarding user comments, liked messages, liked posts, story interactions, and so forth is nonexistent. I have messaged Instagram about this and encourage you to do so yourself, but there is nothing I can do about this at the moment. **Possible fix in progress.**
 - There is no way to determine the name of a conversation from the data. **Fix in progress!**
 - Instagram's images use URL signatures which expire after some unknown amount of time. Because of this, attempting to render an older data download will result in missing media. Because of this, it is recommended to render data downloads as soon as possible.