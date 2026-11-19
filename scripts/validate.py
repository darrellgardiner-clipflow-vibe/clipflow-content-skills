#!/usr/bin/env python3
"""Check public-pack metadata and local references without network or credentials."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"clipflow-content", "clipflow-brand", "clipflow-plan", "clipflow-write", "clipflow-review"}


def validate(root):
    errors = []
    skills = {p.parent.name: p for p in (root / "skills").glob("*/SKILL.md")}
    if set(skills) != EXPECTED:
        errors.append("The pack must contain all five sibling skills")
    for name, path in skills.items():
        text = path.read_text()
        match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not match:
            errors.append(f"{name}: missing frontmatter")
            continue
        header = match.group(1)
        if not re.search(rf"^name: {re.escape(name)}$", header, re.M):
            errors.append(f"{name}: directory and skill name disagree")
        if not re.search(r"^description: \S", header, re.M):
            errors.append(f"{name}: missing description")
        if not re.search(r'^  version: "[0-9]+\.[0-9]+\.[0-9]+"$', header, re.M):
            errors.append(f"{name}: missing metadata version")
    for path in root.rglob("*.md"):
        text = path.read_text()
        if re.search(r"/Users/|/home/|https?://[^\s]+\.ts\.net", text):
            errors.append(f"{path.relative_to(root)}: host-specific path or address")
        if "\u2014" in text:
            errors.append(f"{path.relative_to(root)}: contains a long dash")
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if link.startswith(("https://", "http://", "#", "mailto:")):
                continue
            target = (path.parent / link.split("#")[0]).resolve()
            if not target.is_relative_to(root.resolve()) or not target.exists():
                errors.append(f"{path.relative_to(root)}: unavailable local reference {link}")
    try:
        plugin = json.loads((root / ".claude-plugin/plugin.json").read_text())
        market = json.loads((root / ".claude-plugin/marketplace.json").read_text())
        if plugin["name"] != "clipflow-content" or plugin["license"] != "MIT":
            errors.append("Unexpected plugin identity or license")
        if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", plugin["version"]):
            errors.append("Invalid plugin version")
        if market["name"] != "clipflow-content-skills":
            errors.append("Marketplace name differs from README installation command")
        if market["plugins"][0]["name"] != plugin["name"] or market["plugins"][0]["source"] != "./":
            errors.append("Marketplace must resolve the root plugin")
    except (OSError, ValueError, KeyError, IndexError, TypeError) as exc:
        errors.append(f"Invalid plugin manifests: {exc}")
    return errors


if __name__ == "__main__":
    problems = validate(ROOT)
    for problem in problems:
        print(problem)
    if not problems:
        print("Five skills, plugin manifests and local references pass. Editorial behavior is not checked.")
    raise SystemExit(bool(problems))
