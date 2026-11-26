#!/usr/bin/env python3
"""The Robot Apology — a robot's two-line confession."""

import os

# Two sentences, no newline: the gate requires /output/entry.txt to be UTF-8,
# 1-400 characters. The entry below is 226 characters.
ENTRY = "I'm sorry I sent your resignation letter to the whole office group chat instead of your boss \u2014 I confused 'reply' with 'reply all.' From now on I read the recipient line out loud before I send anything that could end a career."

# Gate check: two sentences, 1-400 characters (byte-identical on every run).
assert 1 <= len(ENTRY) <= 400, f"entry length {len(ENTRY)} outside 1-400"
assert "\n" not in ENTRY, "entry must contain no newline"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
