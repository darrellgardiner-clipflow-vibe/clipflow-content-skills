# Plan next week's content from what you already have online

Give Claude Code or Codex links to videos you've already filmed, your website
or something you've published. The five free Clipflow skills work out what you could post next week, where
each idea comes from and what you need to do first. A single readable page is
enough to start. Recordings, transcripts and pasted posts work too.

## Try this after installing

```text
Use clipflow-content. Here are videos I've already posted: [paste your links].
Turn them into a week of LinkedIn posts, one a day, and write all five. I have
about an hour next week.
```

No videos yet? Swap the links for your website and ask for a plan and a first
draft. If you have a particular account or goal in mind, add it: “For our LinkedIn
page. We want enquiries about kitchen renovations.” If a post sits behind a
login, paste its caption or share a screenshot. Other readable links can
still supply the week.

**What you open first:** `content/week-plan.md`. It names the first post to
make, its source, and the next action. Each proposed post has a reader
question, a format and an estimate for the work still to do. A draft you ask
for is in `content/posts/`.

**See what comes back:** From three videos already on a founder's YouTube
channel, the skills wrote a LinkedIn post for each weekday. Checking and posting
them came to about 50 of the 60 minutes available. Two published articles supplied a text post
and a short video to film.
[YouTube videos example](examples/week-from-youtube-videos.md) ·
[Founder article example](examples/week-from-public-links.md).

## Install in Claude Code

In Claude Code, run:

```text
/plugin marketplace add darrellgardiner-clipflow-vibe/clipflow-content-skills
/plugin install clipflow-content@clipflow-content-skills
```

Open a project folder where you'd like to keep the plan. You can also copy
the five folders inside `skills/` into `~/.claude/skills/` (all projects) or
`.claude/skills/` (one project). Keep the five folders together.

## Install in Codex

Ask Codex:

```text
$skill-installer install the skills in skills/clipflow-content, skills/clipflow-brand,
skills/clipflow-plan, skills/clipflow-write and skills/clipflow-review from
https://github.com/darrellgardiner-clipflow-vibe/clipflow-content-skills
```

Or copy the five folders into `~/.codex/skills/`. Restart Codex, open your
project folder and give it the first prompt above.

## What the five skills do

| Skill | Use it for |
|---|---|
| [clipflow-content](skills/clipflow-content/SKILL.md) | Start here with a link or files. It gathers the material and runs as much of the routine as you ask for. |
| [clipflow-brand](skills/clipflow-brand/SKILL.md) | Get a short brief for the week. Ask for a full profile to get five reusable documents covering the business, likely buyers, voice, offers and proof, and visible design choices. You can correct them. |
| [clipflow-plan](skills/clipflow-plan/SKILL.md) | Choose the week from supported ideas, existing commitments and the time you have. Each post points back to a page, post or passage of footage. |
| [clipflow-write](skills/clipflow-write/SKILL.md) | Draft the piece you choose, from a text post to a reel script, caption or carousel. You can also ask for every supported post in the plan. |
| [clipflow-review](skills/clipflow-review/SKILL.md) | Check wording, attribution, facts and what still needs making. With results you supply, pick one thing to try next week. |

The website notes describe who the pages appear to address. Real customers,
a founder's personal opinions and performance numbers need sources of their
own. Public copy stays separate from the notes and source links in your files.

## Other ways to start

- **Videos or audio files.** Supply the original or captions. An installed local
  transcriber can produce timestamps. The skills ask before installing software
  or uploading recordings. [Material guide](skills/clipflow-content/references/getting-material.md).
- **No public pages or recordings yet.** Answer the short interview or try the
  [sample transcript](examples/README.md).
- **An existing plan.** Ask for one post, a revision, or a review. Next week,
  keep the same folder and say what you published and how much time it took.

The pack saves editable files. You decide what goes out. A Clipflow account is
optional. If you already use it, you can ask your connected agent to save work
as drafts in your calendar. [Clipflow connector](skills/clipflow-content/references/clipflow.md).

Check the pack's structure with `python3 scripts/validate.py`.

Made by Clipflow. [MIT license](LICENSE).
