# InstagramDataRenderer
A tool to render the data downloads provided by Instagram into user-friendly HTML documents for archival purposes.

Requirements: [Python 3.6+](https://www.python.org/downloads/)

Usage: `python render.py FILENAME`

The main file to open in your browser is the index, `index.html`.

All remote resources are embedded in the generated html files — therefore, you will not need to rely on external CDNs to view your data in the future.

## A few issues...

 - At the moment, Instagram's data downloads do not provide adequate information for dealing with users who have changed their name. Because of this, direct messages you have with them may be split into two separate conversations.