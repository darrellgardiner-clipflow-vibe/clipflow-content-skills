---
name: clipflow-content
metadata:
  version: "1.1.0"
description: Coordinate a brand-to-content workflow using skill-based Brand Lens analysis of supplied evidence, with an optional Clipflow connector for requested workspace, scheduling or publishing actions. Use for requests spanning brand understanding, a content week, drafting and review; route single-stage requests to the corresponding clipflow-brand, clipflow-plan, clipflow-write or clipflow-review skill.
---

# Plan and create content for a business

Help a business decide what to make and turn its knowledge, experience and
source material into content its customers will find useful. Carry the business
context through planning, writing and review so the user does not have to
explain it again at each step.

## Start with the business and the job

Read the request and any existing brief or source material. Establish what the
business does, who the content is for, what those people need help with and what
the business wants this piece or plan to achieve. Check where it will appear
and whether it is written as the company or a named person.

Use the material already available: customer questions, product demonstrations,
work examples, interviews, recordings, existing posts or approved brand notes.
A business does not need all of these to begin. If a missing answer would change
the work, ask for it; otherwise state a reasonable working assumption and proceed.
For a single caption or edit, use the relevant context without requiring a full
brand exercise or weekly plan.

Read [the shared handoff](references/handoff.md) to carry decisions and sources
between stages. Resolve the linked skills relative to this file. Installation
and folder-copying instructions are in [installation](references/install.md).

## Route by the requested outcome

| Need | Owner | Result |
|---|---|---|
| Understand a business, audience, offer or voice | [clipflow-brand](../clipflow-brand/SKILL.md) | Source notes, assessed claims and maintained brand/voice knowledge |
| Decide what can be made this week | [clipflow-plan](../clipflow-plan/SKILL.md) | Feasible slots with sources, purpose and production needs |
| Write one selected piece | [clipflow-write](../clipflow-write/SKILL.md) | Format-specific draft, source map and production notes |
| Check a piece or learn from results | [clipflow-review](../clipflow-review/SKILL.md) | Actionable review, or bounded performance findings |

Start at the first incomplete stage needed for the request. Reuse an existing brief or plan; do not repeat onboarding when the answer is already present. Complete all stages the user requested, without adding an approval stop between reversible local stages. A request for a plan alone stops at the plan. A request for one piece does not produce a whole campaign.

The pack includes the methods for source extraction, editorial strategy, rule/voice composition and format-specific writing. Read only the references needed by the stage and format; no private writing library is required.

Use the [Brand Lens skill workflow](../clipflow-brand/SKILL.md) to turn supplied sources into a working brand brief, or reuse an existing brief. Read [sources](references/sources.md) for evidence handling. No separate Brand Lens service is required. When the user requests actions in Clipflow, follow [the Clipflow handoff](references/clipflow.md) using the tools actually connected to their account.

At each handoff preserve the brand/account, evidence references, source dates, standing, open questions, available assets and selected next action. Keep one working record in the existing content project. Report which stages completed, artifact paths and any material gaps. Readiness and publication permission remain separate.

## Usage

- "Understand this business from these transcripts and approved examples."
- "Plan three pieces for next week; I have one recording session."
- "Use the existing brand brief and write slot P2 as a Reel."
- "Review this draft, preserving the deliberate comment-keyword CTA."

Use supplied brand rules and the manual path. When the project has an established writing workflow, follow [project integration](references/project.md). The standalone pack creates planning and writing artifacts. A connected Clipflow account can take supported scheduling or publishing actions when requested; the skills do not provide those services themselves.
