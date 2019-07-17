## General features and changes:

 - Complete all unfinished sections (obviously)
 - Automatically create clickable links in DMs; just search messages for `http[s]://` and embed them in the proper HTML tags.
 - Automatically create links to accounts mentioned, e.g. `@newyorkermag`.
 - Make timestamps nicer looking.
 - Use locally stored DM files if they exist, to save network usage, and to increase image quality

## Support the following message types in DMs:

 - Post sharing

```
{
    "sender": "REDACTED",
    "created_at": "2018-11-25T04:24:39.409261+00:00",
    "media_owner": "REDACTED",
    "media_share_caption": "Caption unavailable.",
    "media_share_url": "REDACTED"
},
```

 - Video call actions

```
{
    "sender": "REDACTED",
    "created_at": "2018-07-07T23:27:19.409185+00:00",
    "video_call_action": "REDACTED started a video call"
},
```

 - Story sharing

```
{
    "sender": "REDACTED",
    "created_at": "2018-11-03T19:30:25.646697+00:00",
    "likes": [
        {
            "username": "REDACTED",
            "date": "2018-11-03T19:35:23.062724+00:00"
        }
    ],
    "story_share": "Shared REDACTED's story",
    "text": "Nice iPhone there"
},
```

 - Secondary media format `media_url`? Should handle the same as `media`...

```
{
    "sender": "REDACTED",
    "created_at": "2019-06-13T02:15:02.150760+00:00",
    "likes": [
        {
            "username": "REDACTED",
            "date": "2019-06-13T02:15:14.329551+00:00"
        }
    ],
    "media_url": "REDACTED"
},
```

 - Profile sharing

```
{
    "sender": "REDACTED",
    "created_at": "2019-02-26T03:44:30.259477+00:00",
    "profile_share_username": "birdsarentreal",
    "profile_share_name": "Birds Aren't Real"
},
```

 - Group actions

```
{
    "sender": "REDACTED",
    "created_at": "2019-02-27T04:19:06.700444+00:00",
    "action": "REDACTED named the group REDACTED"
},
```

 - Voice media

```
{
    "sender": "REDACTED",
    "created_at": "2019-01-15T03:14:34.432961+00:00",
    "likes": [
        {
            "username": "REDACTED",
            "date": "2019-01-15T03:15:15.508752+00:00"
        }
    ],
    "voice_media": "Media unavailable."
},
```

 - GIPHY trash

*The only special entry likely to be relevant here is `animated_media_images["original"]["mp4"]`, as that provides the highest quality image.*

```
{
    "sender": "REDACTED",
    "created_at": "2019-07-10T17:42:56.606391+00:00",
    "likes": [
        {
            "username": "REDACTED",
            "date": "2019-07-10T17:45:23.570420+00:00"
        },
        {
            "username": "REDACTED",
            "date": "2019-07-10T21:55:26.036437+00:00"
        }
    ],
    "animated_media_images": {
        [...]
        "original": {
            "url": "https://media3.giphy.com/media/3kHyZdQMZsxHAr5Rv1.Y2lkPTAyZWZlMmI0NWQyNjIzYTA1MzZhNzY3YTMyNjY5Yjgiphy.gif",
            "width": "480",
            "height": "270",
            "size": "3670579",
            "frames": "37",
            "mp4": "https://media3.giphy.com/media/3kHyZdQMZsxHAr5Rv1.Y2lkPTAyZWZlMmI0NWQyNjIzYTA1MzZhNzY3YTMyNjY5Yjgiphy.mp4",
            "mp4_size": "373061",
            "webp": "https://media3.giphy.com/media/3kHyZdQMZsxHAr5Rv1.Y2lkPTAyZWZlMmI0NWQyNjIzYTA1MzZhNzY3YTMyNjY5Yjgiphy.webp",
            "webp_size": "1005740",
            "hash": "03c662ffe33656eb91d4e703c19106cf"
        },
        [...]
    },
    "is_random": false,
    "user": {}
},
```