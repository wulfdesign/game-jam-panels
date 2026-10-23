#!/usr/bin/env python3
"""
Chat Transcript & Artifact Backup Utility
Copies the active Antigravity session transcript and artifacts to the local archive.
"""
import os
import shutil
import sys

SESSION_ID = "1d4c47d1-3853-45aa-92d1-0558f7dc3325"
SRC_LOGS = os.path.expanduser(f"~/.gemini/antigravity/brain/{SESSION_ID}/.system_generated/logs")
SRC_BRAIN = os.path.expanduser(f"~/.gemini/antigravity/brain/{SESSION_ID}")
DEST_DIR = r"C:\Agents\a0-symbiot-ai\archive\chat_transcripts"
DEST_ARTIFACTS = os.path.join(DEST_DIR, f"artifacts_{SESSION_ID[:8]}")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(DEST_ARTIFACTS, exist_ok=True)

print(f"[*] Backing up session: {SESSION_ID}")

# 1. Compact transcript
src_compact = os.path.join(SRC_LOGS, "transcript.jsonl")
dest_compact = os.path.join(DEST_DIR, f"2026-10-21_geekgirlcon_session_{SESSION_ID[:8]}.jsonl")
if os.path.exists(src_compact):
    shutil.copy2(src_compact, dest_compact)
    size_mb = os.path.getsize(dest_compact) / (1024 * 1024)
    print(f"    [+] Saved transcript.jsonl -> {dest_compact} ({size_mb:.2f} MB)")
else:
    print(f"    [-] Not found: {src_compact}")

# 2. Full transcript
src_full = os.path.join(SRC_LOGS, "transcript_full.jsonl")
dest_full = os.path.join(DEST_DIR, f"2026-10-21_geekgirlcon_session_{SESSION_ID[:8]}_full.jsonl")
if os.path.exists(src_full):
    shutil.copy2(src_full, dest_full)
    size_mb = os.path.getsize(dest_full) / (1024 * 1024)
    print(f"    [+] Saved transcript_full.jsonl -> {dest_full} ({size_mb:.2f} MB)")
else:
    print(f"    [-] Not found: {src_full}")

# 3. Artifacts
for item in os.listdir(SRC_BRAIN):
    if item.endswith(".md"):
        s = os.path.join(SRC_BRAIN, item)
        d = os.path.join(DEST_ARTIFACTS, item)
        shutil.copy2(s, d)
        print(f"    [+] Copied artifact: {item}")

print("[*] Backup complete!")
