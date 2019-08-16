# InstagramDataRenderer
A tool to render the data downloads provided by Instagram into user-friendly HTML documents for archival purposes.

Requirements:
 - [Python 3.7+](https://www.python.org/downloads/) (Needed for ordered dictionaries.)
 - [Requests](https://2.python-requests.org/en/master/)

Usage: `python render.py ArchivePartOne ArchivePartTwo ArchivePartThree <--no-media, -n>`
 - `--no-media`, `-n`: Only text is rendered in conversations / direct messages. Useful if you have friends that spam *way* too many memes or images. Provides a significant speed-up to the overall process.

The main file to open in your browser is the index, `index.html`.

The font used is [Montserrat](https://fonts.google.com/specimen/Montserrat), as I believe this is a good free imitation of Instagram's default web font [Proxima Nova](https://fonts.adobe.com/fonts/proxima-nova).

## Troubleshooting

### Warning `Unable to download resource` for a large volume of messages when rendering direct messages

Consider downloading a new copy of your data. Instagram's content URLs use an internal URL signature which causes them to expire after some indeterminate amount of time, so it is important to render your data as soon as you have downloaded it.

## A few issues

 - The CSS used isn't that great. Any commits regarding that are greatly appreciated!
 - At the moment, Instagram's data downloads do not provide adequate information for dealing with users who have changed their name. Because of this, direct messages you have with them may be split into two separate conversations.
 - There is no proper way to determine continuity between conversations if users leave or join them. Because of this, a single conversation may be rendered as multiple conversations.
 - Instagram's images use URL signatures which expire after some unknown amount of time. Attempting to render an older data download will result in missing media. Because of this, it is recommended to render data downloads as soon as possible.
 - Comments on posts cannot be rendered well because they lack full context. The only information Instagram provides is a timestamp, post uploader name, and the user's comment itself.
 - Liked posts cannot be rendered well because they lack full context. The only information Instagram provides is a timestamp and uploader name.
 - User posts cannot be rendered well because they lack full context. No information is provided regarding comments or likes.
   - Also, some posts mentioned in `media.json` don't exist as files for some odd reason. #BlameInstagram

## A few complete failures

 - Liked comments on posts cannot be rendered. No data is provided regarding this.