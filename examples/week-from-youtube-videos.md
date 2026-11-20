# Five LinkedIn posts from three YouTube videos

In a test run on 20 November 2026, we gave the skills links to three videos
already on Darrell Gardiner's YouTube channel and asked for a week of posts on
his personal LinkedIn. Nothing new was filmed. The days are proposals, and the
time estimates cover the work left for Darrell. The run used Claude Opus in
Claude Code. Smaller models follow the same steps, but their drafts need more
editing.

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
into transcripts and saved them in `content/sources/`. Every post cites the
minutes it came from.

## The week of 23 November

| Day | Post | Where it came from | What remains |
|---|---|---|---|
| Monday | The thumbnail that broke every rule | [Audience building video](https://www.youtube.com/watch?v=TvtKVtVmQb4&t=99s), from 1:39 | Check the view and subscriber numbers against the channel, then post. About 7 minutes. |
| Tuesday | Pitching ideas in one sentence | [Starting a business video](https://www.youtube.com/watch?v=LhLOjs8-rjI&t=360s), 6:00 to 7:06 | Ready to post. About 5 minutes. |
| Wednesday | What one email to Time magazine was worth | [Email video](https://www.youtube.com/watch?v=_6QJEpaUjRE&t=35s), 0:35 to 5:04 | Find Tyler Denk's original post and check the case study figures. About 15 minutes. |
| Thursday | Reels that shaped Clipflow's product | [Audience building video](https://www.youtube.com/watch?v=TvtKVtVmQb4&t=370s), 6:10 to 6:44 | Ready to post, once he's happy saying publicly which features came from Reels. About 5 minutes. |
| Friday | Managers and sightlines | [Starting a business video](https://www.youtube.com/watch?v=LhLOjs8-rjI&t=294s), 4:54 to 6:00 | Decide whether to end on the hiring line from the video. About 8 minutes. |

**Make Wednesday's post first**, because it's the only one that leans on
someone else's numbers. All five came back written, so reading, checking and
posting them comes to about 40 of the 60 minutes.

## Tuesday's draft, as it came back

> I used to pitch ideas in one sentence, then get upset when nobody listened.
>
> In my last business, I'd hear a no and assign all my anxieties to it. I'm
> terrible. I'm evil. No one likes me. No one likes my suggestions.
>
> None of that was true. I just wasn't explaining things well enough. I'd go
> through every mechanism in my head for why something was a good idea, and
> then when it came time to sell it, I'd dump it as one sentence. Anyone in
> their right mind wouldn't have listened, because they hadn't thought through
> all the data, the options and the strategy that I had.
>
> Old me also stayed quiet in meetings. Someone else would speak up and I'd let
> go of things I cared about. "Ah, it's fine. Whatever. They'll know better."
>
> I'm not hugely different to the person who was shutting down in those
> meetings. What I have now is years of confirmation that I might know what I'm
> talking about. If I'd had that confidence back then, I probably would have
> produced better results for the business.
>
> When you care about something, don't let it go just because someone less
> familiar with it speaks up.

The post keeps Darrell's words from the video and drops the filler. It ends on
his own instruction from 6:32 rather than the video's sign-off.

## What the skills caught

- In the email video, Darrell estimates each newsletter was worth $50,000 to
  $133,000 to Beehiiv. The top end doesn't follow from his own figures
  ($1.5 million over nine emails is about $166,000), so Wednesday's draft uses
  only the low end and the notes say why. It also drops a LinkedIn cost-per-lead
  comparison that had no source.
- Monday's video said "last night". The draft opens without it, so the post
  still reads true a few months later.
- Friday's video mentions working out of a garage. The draft leaves that out in
  case it's no longer true, and offers the video's hiring line as an optional
  ending.

## Try it with your videos

Swap in links to your own videos, the account you post on and the time you
have. Public YouTube videos usually come with automatic captions. For a file on
your computer, the skills make a transcript if a transcription tool is
installed, and ask before sending a recording anywhere else.
