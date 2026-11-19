# Clipflow content skills

Skills for Claude Code and Codex that turn the videos, recordings and posts a
business already has into a week of content it can actually make.

Hand over a few recordings (Instagram Lives, client calls, YouTube videos,
podcast episodes, a voice memo) plus some past posts, and ask what to post. You
get back a folder with:

- **A one-page brief:** who you sell to, the questions customers ask, the
  stories you tell, how you talk, and what's missing.
- **A week plan** that fits the time you have, with a mix of posts that bring
  enquiries and posts that build trust, and backups if one falls through.
- **Finished posts:** reel scripts or clip trim times from your own footage,
  on-screen text, carousels slide by slide, and captions ready to paste.
- **A list of questions to answer next time you film**, so next week has
  material too.

Everything comes from your own material. It won't invent reviews, client
stories, numbers or results, and it doesn't post anything for you.

| Skill | What it does |
|---|---|
| [clipflow-content](skills/clipflow-content/SKILL.md) | The front door. Works out what you've got and runs the rest |
| [clipflow-brand](skills/clipflow-brand/SKILL.md) | Reads your material and writes the brief |
| [clipflow-plan](skills/clipflow-plan/SKILL.md) | Finds post ideas in your recordings and plans the week |
| [clipflow-write](skills/clipflow-write/SKILL.md) | Writes each post in your voice |
| [clipflow-review](skills/clipflow-review/SKILL.md) | Checks and fixes every post, and reads your results |

## Install in Claude Code

In Claude Code, run:

```text
/plugin marketplace add darrellgardiner-clipflow-vibe/clipflow-content-skills
/plugin install clipflow-content@clipflow-content-skills
```

Or copy the five folders inside `skills/` into `~/.claude/skills/` (for every
project) or `.claude/skills/` inside one project. Keep all five together; they
link to each other.

## Install in Codex

Ask Codex:

```text
$skill-installer install the skills in skills/clipflow-content, skills/clipflow-brand,
skills/clipflow-plan, skills/clipflow-write and skills/clipflow-review from
https://github.com/darrellgardiner-clipflow-vibe/clipflow-content-skills
```

Or copy the five folders into `~/.codex/skills/`. Restart Codex afterwards.

## First prompt

Put your files in a folder, open Claude Code or Codex there, and ask:

```text
Use clipflow-content. Here are my last three Instagram Lives and ten of my past
posts. Plan this week's posts and write them. I've got about an hour.
```

It reads everything, asks at most one round of questions, and hands back the
`content/` folder with a short summary of what to film, trim or check.

You can also ask for one thing: "Write a caption for this reel", "Turn the bit
at 12:40 into a carousel", "Is this post any good?", or share a screenshot of
your insights and ask how your posts did.

No recordings yet? Say so. It asks you ten questions about your business, and
your answers become the material.

No material at all to test with? Use the [sample transcript](examples/README.md).

## Video and audio

Claude and Codex can't watch a video. The skills transcribe it on your
computer with [whisper.cpp](https://github.com/ggml-org/whisper.cpp) or
OpenAI's Whisper if you have either installed. If you don't, they'll ask before
installing anything, or you can paste in the auto-captions from YouTube or
Instagram. Nothing is uploaded anywhere without asking you first.

## Clipflow

If you use [Clipflow](https://clipflow.co) and connect it to your agent, the
skills can put the finished posts into your content calendar, as drafts unless
you ask for more. The skills work fully without it.

## What it doesn't do

It doesn't post, schedule, edit video, design slides or predict views. It
writes what to film, where to trim and what to paste. It's been tested on a
handful of real and made-up businesses' material in Claude Code; treat the
first week's output as a draft you check, especially facts and prices.

Check the pack's structure with `python3 scripts/validate.py`.

## License

Made by Clipflow. [MIT license](LICENSE).
