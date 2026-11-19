# Optional Clipflow connector

Use the skills for brand analysis, planning, writing and review without a
connection. When the user asks to save work in Clipflow, schedule or publish,
use the tools exposed by their connected Clipflow account. This repository
contains workflow instructions, not a publishing service or authentication client.

## Resolve the connection and target

Discover the available tools and inspect their input schemas. Use read-only
account/workspace/channel discovery to identify the intended organization and
destination. Reuse known, verified IDs from the current project. Do not invent
an endpoint, tool name or permission, or assume that a similarly named account
is the target. Use the provider's supported connection flow when access is
missing; do not ask for passwords or put credentials in briefs.

If the requested action is unsupported or the connection is unavailable,
complete the authorized local work and report the missing capability. Hand back
the draft and intended destination without claiming it was saved or published.

## Carry the reviewed work into Clipflow

Resolve the requested action separately: create/update a draft, schedule, or
publish. A request to plan or review content does not itself authorize those
external actions. Use authorization already present in the conversation; do
not ask again when the user has clearly authorized the specific action.

Before a mutation, check the selected copy and assets against the review,
verify the organization/channel, and resolve the intended timing and timezone
for a schedule. Honour existing approvals and hold unresolved factual or
fulfilment dependencies. Do not overwrite unrelated posts or calendar entries.
Use the connected tool's supported fields and actions rather than assuming
that creating a post also schedules or publishes it.

Record the returned post/media identifiers, requested action and actual state
in the current piece record. Read back the result using the connector's
supported status/lookup tool when available. A successful create response is
not proof of publication. If an action times out, inspect its state before
retrying so the same post is not published twice. If verification is unavailable,
report the response received and the unverified outcome plainly.

This guide does not grant permission to publish, schedule, message audiences
or change brand/account settings beyond the user's request.
