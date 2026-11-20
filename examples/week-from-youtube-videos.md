# Five LinkedIn posts from three YouTube videos

In a test run on 20 November 2026, we gave the skills links to three videos
already on Darrell Gardiner's YouTube channel and asked for a week of posts on
his personal LinkedIn. Nothing new was filmed. The days are proposals, and the
time estimates cover the work left for Darrell.

```text
Use clipflow-content. These are three videos I've already posted on my YouTube
channel:
https://www.youtube.com/watch?v=TvtKVtVmQb4
https://www.youtube.com/watch?v=_6QJEpaUjRE
https://www.youtube.com/watch?v=LhLOjs8-rjI
Turn them into a week of LinkedIn posts for my personal account, one a day
Monday to Friday, and write all five. I've got about an hour next week to post them.
```

The agent pulled each video's automatic captions with `yt-dlp`, cleaned them
into transcripts and saved them in `content/sources/`. It fixed caption
mishearings ("Might Shyamalan" became M. Night Shyamalan) and noted each fix.

## The week of 23 November

| Day | Post | Where it came from | What remains |
|---|---|---|---|
| Monday | A first video with broken packaging got 1.6M views in four days | [Audience building video](https://www.youtube.com/watch?v=TvtKVtVmQb4), 0:00 to 3:49 | Check the view and subscriber figures against the video, then post. About 12 minutes. |
| Tuesday | Time's CTO read one founder's emails for six months | [Email video](https://www.youtube.com/watch?v=_6QJEpaUjRE&t=35s), 0:35 to 8:52 | Check the newsletter figures against the case study. About 12 minutes. |
| Wednesday | A solo kid in a bedroom could build your app in a weekend | [Starting a business video](https://www.youtube.com/watch?v=LhLOjs8-rjI&t=98s), 1:38 to 2:43 | Confirm the team still works out of the garage, or change that line to the past tense. About 8 minutes. |
| Thursday | Which Reels people reacted to decided what we built | [Audience building video](https://www.youtube.com/watch?v=TvtKVtVmQb4&t=359s), 5:59 to 6:32 | Ready to post. It refers back to Monday's post. About 8 minutes. |
| Friday | Old me in the bin | [Starting a business video](https://www.youtube.com/watch?v=LhLOjs8-rjI&t=355s), 5:55 to 7:00 | Ready to post. About 8 minutes. |

**Make Monday's post first.** All five posts came back written, so the plan
used about 50 of the 60 minutes on checking facts and posting. Four more ideas
from the starting-a-business video sit in `content/ideas.md` as backups.

## From Friday's draft

> In my last business I'd think an idea all the way through, then pitch it in
> one sentence and get really upset when nobody wanted to listen.
>
> I'd have gone through the data, the options and the strategy in my head.
> Nobody else had.

Every figure and name in the five posts matches what Darrell says in the
videos: 1.6 million views and over 100,000 subscribers in four days, Burhan
Hamid reading the newsletter for six months, 2 million subscribers across 13
newsletters with zero downtime, and five offices across three countries.
The Tuesday video also gives a dollar calculation that doesn't add up, so the
skills left it out and said why in the post's notes.

## Try it with your videos

Swap in links to your own videos, the account you post on and the time you
have. Public YouTube videos usually come with automatic captions. For a file on
your computer, the skills make a transcript if a transcription tool is
installed, and ask before sending a recording anywhere else.
