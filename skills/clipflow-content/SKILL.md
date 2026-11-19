---
name: clipflow-content
metadata:
  version: "1.0.1"
description: Coordinate a brand-to-content workflow using skill-based Brand Lens analysis of supplied evidence, with an optional Clipflow connector for requested workspace, scheduling or publishing actions. Use for requests spanning brand understanding, a content week, drafting and review; route single-stage requests to the corresponding clipflow-brand, clipflow-plan, clipflow-write or clipflow-review skill.
---

# Content from brand evidence

Turn a request such as "use our recent recordings to plan next week and write Tuesday" into connected work with one shared brief. This pack supports any brand; its name does not select Clipflow as the speaker.

Read [the shared handoff](references/handoff.md) first. Resolve sibling skills relative to this folder, never from the shell's working directory. Keep all five `clipflow-*` folders together when copying the pack. See [installation](references/install.md) when registering or copying them.

## Route by the requested outcome

| Need | Owner | Result |
|---|---|---|
| Understand a business, audience, offer or voice | [clipflow-brand](../clipflow-brand/SKILL.md) | Evidence-backed brand brief with unknowns |
| Decide what can be made this week | [clipflow-plan](../clipflow-plan/SKILL.md) | Feasible slots with sources, purpose and production needs |
| Write one selected piece | [clipflow-write](../clipflow-write/SKILL.md) | Draft, source map and production notes |
| Check a piece or learn from results | [clipflow-review](../clipflow-review/SKILL.md) | Actionable review, or bounded performance findings |

Start at the first incomplete stage needed for the request. Reuse an existing brief or plan; do not repeat onboarding when the answer is already present. Complete all stages the user requested, without adding an approval stop between reversible local stages. A request for a plan alone stops at the plan. A request for one piece does not produce a whole campaign.

Use the [Brand Lens skill workflow](../clipflow-brand/SKILL.md) to turn supplied sources into a working brand brief, or reuse an existing brief. Read [sources](references/sources.md) for evidence handling. No separate Brand Lens service is required. When the user requests actions in Clipflow, follow [the Clipflow handoff](references/clipflow.md) using the tools actually connected to their account.

At each handoff preserve the brand/account, evidence references, source dates, standing, open questions, available assets and selected next action. Keep one working record in the existing content project. Report which stages completed, artifact paths and any material gaps. Readiness and publication permission remain separate.

## Usage

- "Understand this business from these transcripts and approved examples."
- "Plan three pieces for next week; I have one recording session."
- "Use the existing brand brief and write slot P2 as a Reel."
- "Review this draft, preserving the deliberate comment-keyword CTA."

Use supplied brand rules and the manual path. When the project has an established writing workflow, follow [project integration](references/project.md). The standalone pack creates planning and writing artifacts. A connected Clipflow account can take supported scheduling or publishing actions when requested; the skills do not provide those services themselves.
