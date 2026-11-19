# Files and templates

Everything lives in one `content/` folder (or the folder the owner names):

```text
content/
  brief.md          who they are, who they sell to, how they talk
  ideas.md          every post idea found so far, kept between weeks
  week-plan.md      this week's posts and what to do for each
  posts/
    01-friday-neck.md
    02-...
  sources.md        list of every source and its tag
  sources/          clean transcripts and raw caption files
  results.md        only when they've shared post results
```

If the folder exists, read it before writing. Update sections in place, add
new ideas to the bottom of `ideas.md`, and start a new dated section in
`week-plan.md` for a new week. Never delete what they wrote.

## Source tags

Give each source a short tag and list it in `sources.md`:

```markdown
| Tag | What it is | Date | File |
|---|---|---|---|
| S1 | Instagram Live, "Desk neck Q&A" | 2026-10-02 | sources/live-desk-neck.md |
| S2 | 12 past Instagram captions | 2026-08 to 2026-11 | sources/past-posts.md |
| Owner | Things they told you in this chat | 2026-11-19 | |
```

Point at sources like `[S1 12:40]` or `[S1 12:40-13:55]` for transcripts,
`[S2]` for documents, `[Interview Q3]` and `[Owner]`. Tags go in the brief, the
plan and the notes under each post. They never go inside copy that will be posted.

## brief.md

Aim for one page. Short, specific lines beat full sections of guesses.

```markdown
# <Business> brief
Updated <date> from S1, S2, Owner.

## What they sell
## Who it's for
The customer they want more of, in a sentence or two, with what's going on in
that person's life when they go looking.

## What customers ask before buying
Their words, not marketing words. One per line with a tag.

## Stories they can tell
One line each: what happened, and the tag to find it.

## What they believe that others in their industry don't
## Proof they can use
Numbers, results, reviews and credentials they actually gave you, with tags.
### Don't claim
Things a post might want to say that the material doesn't support.

## How they talk
3 to 6 observations, each with a real line of theirs as the example.
Phrases they use:
Words or styles they'd never use:

## What to ask people to do
The action, and exactly where it happens (link in bio, DM a word, call).

## Gaps
What you couldn't find, and the question to answer on camera to fill it.
```

## ideas.md

```markdown
| # | Idea (as a hook) | Kind | From | Format | Used |
|---|---|---|---|---|---|
| 1 | "Why does my neck hurt more on Fridays?" | Customer question | S1 12:40-13:55 | Clip | Week of 24 Nov |
```

## week-plan.md

```markdown
# Week of <date>
Time this week: <what they said, or your assumption>. Posting to: <platforms>.

| # | Post | Format | Job | Time | Ask |
|---|---|---|---|---|---|
| 1 | Why your neck hurts more on Fridays | Reel, clipped from S1 | Brings enquiries | 25 min | Book a Thursday assessment |

## 1. <working title>
- **Hook:** the first line, spoken or on screen
- **Why this one:** the customer question or job it does, in one sentence
- **Made from:** `[S1 12:40-13:55]` clipped as is / new 40-second talking video / text only
- **To do:** concrete steps, for example "Trim S1 from 12:40 to 13:55, add the on-screen text from the post file"
- **Ask:** what to tell viewers to do

## Backups
Two or three ready ideas from ideas.md if one of these falls through.

## Next time you film
5 to 8 questions to answer on camera. Pick them to fill the brief's gaps and
to give next week its posts.
```

## posts/NN-slug.md

```markdown
# <working title>
<Platform and format> · <length or slide count> · Post <n> in week of <date>

## Hook options
1. ... (chosen, because ...)
2. ...
3. ...

## Script
(Reel or video: the spoken words. For a clip, the words as said, with the trim points.)

## On-screen text
| When | Text |
|---|---|

## Slides
(Carousel only: slide by slide.)

## Caption
(Ready to paste.)

---
## Notes (not for posting)
- Made from:
- To film or find:
- Check before posting:
- Review: (from clipflow-review)
```

Leave out sections the format doesn't use. A text post has no script or
on-screen text; a carousel has slides and a caption.

## results.md

```markdown
# Results, <date range>
| Post | Date | Format | Views | <their measures: DMs, enquiries, clicks, saves...> | vs their usual |
|---|---|---|---|---|---|

What stood out:
Try next week:
```
