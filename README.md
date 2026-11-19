# Clipflow content skills

Five agent skills to help a business understand its audience and voice, decide
what content to make, write it and review it. Start with the material you have:
customer questions, work examples, product information, posts, recordings or
transcripts. The Brand Lens workflow runs as skills; connect Clipflow when
you want to take the finished work into your content calendar and publishing.

The same brief and evidence travel through the workflow, so you do not have
to explain the audience, voice and offer again at every step.

| Skill | What it does |
|---|---|
| [clipflow-content](skills/clipflow-content/SKILL.md) | Coordinates the stages needed for your request |
| [clipflow-brand](skills/clipflow-brand/SKILL.md) | Builds a brand and voice brief from evidence |
| [clipflow-plan](skills/clipflow-plan/SKILL.md) | Plans a feasible week around your sources and capacity |
| [clipflow-write](skills/clipflow-write/SKILL.md) | Writes a selected script, caption, carousel or article |
| [clipflow-review](skills/clipflow-review/SKILL.md) | Checks a draft or interprets supplied performance results |

## Methods included

The pack contains the working methods behind the five entry points, so you do
not need a separate private writing system:

- [Brand Lens extraction](skills/clipflow-brand/references/extraction.md): source
  inventory, grounded observations, assessed claims, audience/voice knowledge,
  evidence coverage and dated refreshes.
- [Editorial decisions](skills/clipflow-write/references/editorial-method.md):
  interpreting the request, choosing a reader question and angle, outlining,
  and extracting distinct pieces from one source.
- [Voice and scoped rules](skills/clipflow-write/references/voice-and-rules.md):
  learning from samples and approved edits, keeping author/account/format choices
  separate, and resolving conflicting feedback.
- [Content patterns](skills/clipflow-write/references/patterns.md): explanations,
  decisions, case studies, reactions, comparisons, offers, updates and resolution.
- [Editorial review](skills/clipflow-review/references/editorial-review.md):
  source checks, structure, mechanical and semantic reads, production dependencies,
  and learning from corrections and measured results.

The writer includes dedicated guides for [short video](skills/clipflow-write/references/formats/short-video.md),
[carousels](skills/clipflow-write/references/formats/carousel.md),
[social posts and captions](skills/clipflow-write/references/formats/social.md),
[articles and essays](skills/clipflow-write/references/formats/article.md),
[email](skills/clipflow-write/references/formats/email.md),
[long video](skills/clipflow-write/references/formats/long-video.md),
[sales copy](skills/clipflow-write/references/formats/sales-copy.md), and
[help content](skills/clipflow-write/references/formats/help.md).
Read only the method needed for the current task.

## Try it

Give your agent the repo URL and ask:

```text
Read the clipflow-content skill and its references from this repository.
Understand my brand from these documents, plan two pieces for next week,
write the first, and review it. I have 45 minutes and no new recording time.
Preserve my deliberate CTA. Use only the sources I supply.
```

You can also enter a stage directly:

```text
Use clipflow-review to check this draft against its brief and sources.
Keep the comment-keyword CTA. Tell me if anything promised is missing.
```

Try the fictional [Cedar Desk brief](examples/cedar-desk.md) for a short local
trial. [Harbour Mill](examples/harbour-mill.md) exercises brand analysis, a video,
a carousel and a knowledge refresh; [Orbit Studio](examples/orbit-studio.md)
exercises an article, email, a narrow edit and a results review. These examples
contain no real customer information. See [running the examples](examples/README.md).

## Install in Claude Code

Add the repository as a plugin marketplace, then install the plugin:

```text
/plugin marketplace add darrellgardiner-clipflow-vibe/clipflow-content-skills
/plugin install clipflow-content@clipflow-content-skills
```

The plugin contains all five skills. With a plugin namespace, Claude Code may
show the entry point as `/clipflow-content:clipflow-content`; use the command
name displayed by your installed version.

For manual installation, clone this repository and copy all five folders from
`skills/` into your agent's configured skills directory. Keep them together
and check for existing same-named skills before copying. The pack also works
when an agent reads the `SKILL.md` files directly.

## Inputs and outputs

Start with what you have: approved brand documents, accepted and rejected copy,
transcripts, customer questions, current offer facts, available assets and your
production budget. Missing optional facts stay unknown rather than being filled
with invented numbers.

The workflow produces a brand brief with grounded notes and claims as needed,
a plan with source-backed slots, format-specific drafts and an editorial review.
A [brand record](skills/clipflow-brand/references/records.md) and
[piece brief](skills/clipflow-write/references/brief.md) provide reusable fields
when no existing project structure is available. It can reuse your current
folder and calendar.
Public copy stays separate from production notes and evidence.

A deliberate save, reply, follow, booking or comment-keyword CTA is preserved.
If its promised asset is unfinished, the draft can be complete while fulfilment
remains blocked. No automatic humanizer rewrites your meaning to raise a score.

## Brand Lens skills and the Clipflow connector

- **Brand Lens, as skills:** the included [clipflow-brand](skills/clipflow-brand/SKILL.md)
  workflow reads your source material, extracts evidence and builds a working
  picture of your audience, positioning, voice, offers and proof. It runs from
  files in your project, without a separate Brand Lens service or account.
  An existing brand brief can be supplied directly when you already have one.
- **Clipflow, as an optional connector:** connect your Clipflow account to bring
  the plan and finished content into your workspace. The agent can use available
  Clipflow tools to create or update posts, schedule them or publish when you
  request those actions. See [the Clipflow handoff](skills/clipflow-content/references/clipflow.md).

Existing brand rules, channel writers and required reviews remain in control.
See [project integration](skills/clipflow-content/references/project.md).
The standalone path needs no API key. Your agent provider and any connected
services retain their own costs and access requirements. This pack does not
bundle a Clipflow connection or credentials; use the tools exposed by your
connected account.

## Scope and validation

On its own, this pack understands the brand, plans, writes and reviews. It does
not publish, schedule, collect analytics, render carousels or edit video by
itself. Connect Clipflow to take supported actions such as scheduling and
publishing, within your account permissions and the scope you request.
It does not predict views or detect AI authorship.

Standalone tests used two fictional businesses with no private writing library:
Harbour Mill produced brand knowledge, a plan, short video, carousel/caption and
a later knowledge refresh. Orbit Studio produced brand knowledge, an article,
newsletter, narrow caption edit and a results review. These tests exercised
duplicate evidence, author/company voice, corrected offers, missing fulfilment
and unequal analytics windows. An earlier Cedar Desk trial covered a first post
and an unfinished CTA resource.

These are limited text-based exercises, not proof across every business or format.
Long-video, sales-copy and help guides have source/structure review but were not
independently exercised in those runs. Audio, rendered visuals, provider UI
installation and connected Clipflow publishing remain outside that test evidence.

Check skill metadata, plugin manifests and local references with:

```sh
python3 scripts/validate.py
```

Structural checks do not prove editorial quality. Verify actual generated work
against its brief, sources and the selected format before the next action.

## Contributing

Keep each skill focused and preserve the shared handoffs. Include a realistic
example when reporting a failure, with private information removed. Check local
links and metadata before sending a change. Do not commit customer source material,
credentials or generated client drafts.

## License

Created by Clipflow. [MIT license](LICENSE).
