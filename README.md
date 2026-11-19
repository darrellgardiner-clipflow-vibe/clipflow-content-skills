# Clipflow content skills

Five connected agent skills for understanding a brand, planning content,
writing a piece and reviewing it. Use your own documents, posts, recordings
and transcripts. Brand Lens is optional.

The same brief and evidence travel through the workflow, so you do not have
to explain the audience, voice and offer again at every step.

| Skill | What it does |
|---|---|
| [clipflow-content](skills/clipflow-content/SKILL.md) | Coordinates the stages needed for your request |
| [clipflow-brand](skills/clipflow-brand/SKILL.md) | Builds a brand and voice brief from evidence |
| [clipflow-plan](skills/clipflow-plan/SKILL.md) | Plans a feasible week around your sources and capacity |
| [clipflow-write](skills/clipflow-write/SKILL.md) | Writes a selected script, caption, carousel or article |
| [clipflow-review](skills/clipflow-review/SKILL.md) | Checks a draft or interprets supplied performance results |

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

A [fictional sample brief](examples/cedar-desk.md) is included for a local trial.

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

The workflow produces a brand brief, a plan with source-backed slots, a selected
draft and a review. It can reuse an existing project folder and calendar.
Public copy stays separate from production notes and evidence.

A deliberate save, reply, follow, booking or comment-keyword CTA is preserved.
If its promised asset is unfinished, the draft can be complete while fulfilment
remains blocked. No automatic humanizer rewrites your meaning to raise a score.

## Optional connections

- **Brand Lens:** use your deployment's maintained brand evidence through tools,
  a documented API/CLI or an export. No account or connector is bundled.
- **Content Radar:** supply other-account research as an export or through tools
  available in your environment. This repository does not implement a connector.
- **Your writing system:** existing brand rules, channel writers and required
  reviews remain in control. See [project integration](skills/clipflow-content/references/project.md).

The standalone path needs no API key. Your agent provider and any optional
services retain their own costs and access requirements.

## Scope and validation

This pack plans and writes. It does not publish, schedule, collect analytics,
render carousels or edit video. It does not predict views or detect AI authorship.
The private hook archive and internal company material are not included.

The source workflow was exercised on a fictional brand through brand briefing,
two-slot planning, one draft, review and direct review of a short comment.
Checks covered a retired offer, an unsupported competitor claim, a deliberate
CTA and an unfinished promised asset. Plugin manifests and local references
are checked with:

```sh
python3 scripts/validate.py
```

Provider UI installation and optional connected services need verification in
your own environment. A structural check does not prove editorial quality.

## Contributing

Keep each skill focused and preserve the shared handoffs. Include a realistic
example when reporting a failure, with private information removed. Check local
links and metadata before sending a change. Do not commit customer source material,
credentials or generated client drafts.

## Credit and license

Created by Clipflow. The packaging was inspired by Jake Schincariol's
[Instagram agent skill](https://github.com/Jakeschincariol/instagram-agent-skill).
This repository contains Clipflow's workflow instructions; no hook dataset or
Python tools from that repository are bundled.

[MIT license](LICENSE).
